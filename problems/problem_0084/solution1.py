import numpy as np

DICE_MAX_VALUE = 4

BOARD_VALID_POSITIONS = list(i for i in range(40))
CHANCE_CARD_POSITIONS = [7, 22, 36]
COMMUNITY_CHEST_CARD_POSITIONS = [2, 17, 33]

DICE_PROBA = 1 / (DICE_MAX_VALUE ** 2)
THROWING_ONE_DOUBLE_PROBA = DICE_PROBA
THROWING_ANY_DOUBLE_PROBA = DICE_MAX_VALUE * DICE_PROBA
STAYING_IN_JAIL_PROBA = 1 - THROWING_ANY_DOUBLE_PROBA

DICE_POS_COMBINATION = np.array(list(range(1, DICE_MAX_VALUE + 1)) + list(range(DICE_MAX_VALUE - 1, 0, -1)))
DICE_POS_DOUBLE_COMBINATION = np.array([1] + [0, 1] * (DICE_MAX_VALUE - 1))
THROWING_NON_DOUBLE_PROBA = np.concatenate(([0, 0], DICE_POS_COMBINATION - DICE_POS_DOUBLE_COMBINATION)) * DICE_PROBA

to_jail = lambda pos: 10 if pos == 30 else pos

TRANSITION_THROWING_NON_DOUBLE = [
    ((doubles, board_pos), (0, to_jail((board_pos + dice_value) % 40)), THROWING_NON_DOUBLE_PROBA[dice_value])
    for dice_value in range(3, DICE_MAX_VALUE * 2)
    for board_pos in BOARD_VALID_POSITIONS
    for doubles in range(3)
]

TRANSITION_THROWING_DOUBLE = [
    ((doubles, board_pos), (doubles + 1, to_jail((board_pos + dice_value * 2) % 40)), THROWING_ONE_DOUBLE_PROBA)
    for dice_value in range(1, DICE_MAX_VALUE + 1)
    for board_pos in BOARD_VALID_POSITIONS
    for doubles in range(2)
]

TRANSITION_THROWING_DOUBLE_TO_JAIL = [
    ((2, board_pos), (0, 10), THROWING_ANY_DOUBLE_PROBA) for board_pos in BOARD_VALID_POSITIONS
]

TRANSITION_DICE = (
    TRANSITION_THROWING_NON_DOUBLE,
    TRANSITION_THROWING_DOUBLE,
    TRANSITION_THROWING_DOUBLE_TO_JAIL,
)


def get_card_transition_states(card_position, destination, proba, doubles_out=None):
    return [
        ((doubles, pos), (doubles if doubles_out is None else doubles_out, destination(pos)), proba)
        for pos in card_position
        for doubles in range(3)
    ]


def get_chance_card_transition_states(destination, proba, doubles_out=None):
    return get_card_transition_states(CHANCE_CARD_POSITIONS, destination, proba, doubles_out)


def get_community_chest_card_transition_states(destination, proba, doubles_out=None):
    return get_card_transition_states(COMMUNITY_CHEST_CARD_POSITIONS, destination, proba, doubles_out)


TRANSITION_CHANCE_CARD_STAY = get_chance_card_transition_states(lambda pos: pos, 6 / 16)
TRANSITION_CHANCE_CARD_GO = get_chance_card_transition_states(lambda _: 0, 1 / 16)
TRANSITION_CHANCE_CARD_JAIL = get_chance_card_transition_states(lambda _: 30, 1 / 16, 0)
TRANSITION_CHANCE_CARD_C1 = get_chance_card_transition_states(lambda _: 11, 1 / 16)
TRANSITION_CHANCE_CARD_E3 = get_chance_card_transition_states(lambda _: 24, 1 / 16)
TRANSITION_CHANCE_CARD_H2 = get_chance_card_transition_states(lambda _: 39, 1 / 16)
TRANSITION_CHANCE_CARD_R1 = get_chance_card_transition_states(lambda _: 5, 1 / 16)
TRANSITION_CHANCE_CARD_NEXT_R = get_chance_card_transition_states(lambda pos: {7: 15, 22: 25, 36: 5}[pos], 2 / 16)
TRANSITION_CHANCE_CARD_NEXT_U = get_chance_card_transition_states(lambda pos: {7: 12, 22: 28, 36: 12}[pos], 1 / 16)
TRANSITION_CHANCE_CARD_BACK_3 = get_chance_card_transition_states(lambda pos: pos - 3, 1 / 16)

TRANSITION_COMMUNITY_CHEST_CARD_GO = get_community_chest_card_transition_states(lambda _: 0, 1 / 16)
TRANSITION_COMMUNITY_CHEST_CARD_JAIL = get_community_chest_card_transition_states(lambda _: 10, 1 / 16, 0)
TRANSITION_COMMUNITY_CHEST_CARD_STAY = get_community_chest_card_transition_states(lambda pos: pos, 14 / 16)

TRANSITION_CARD = (
    TRANSITION_CHANCE_CARD_STAY,
    TRANSITION_CHANCE_CARD_JAIL,
    TRANSITION_CHANCE_CARD_GO,
    TRANSITION_CHANCE_CARD_C1,
    TRANSITION_CHANCE_CARD_E3,
    TRANSITION_CHANCE_CARD_H2,
    TRANSITION_CHANCE_CARD_R1,
    TRANSITION_CHANCE_CARD_NEXT_R,
    TRANSITION_CHANCE_CARD_NEXT_U,
    TRANSITION_CHANCE_CARD_BACK_3,
    TRANSITION_COMMUNITY_CHEST_CARD_GO,
    TRANSITION_COMMUNITY_CHEST_CARD_JAIL,
    TRANSITION_COMMUNITY_CHEST_CARD_STAY,
)


def to(doubles, position):
    return doubles * 40 + position


def get_markov():
    dice_transition = np.zeros((120, 120), dtype=np.float64)
    for transition in TRANSITION_DICE:
        for (current_state, next_state, proba) in transition:
            dice_transition[to(*current_state), to(*next_state)] += proba

    for i in (range(120)):
        if not np.isclose(np.sum(dice_transition[i, :]), 1):
            print(i, np.sum(dice_transition[i, :]), dice_transition[i, :])
            assert False

    # Probability of staying at the same position is 1 if the player is not on a card position
    card_transition = np.identity(120, dtype=np.float64)
    card_positions = np.array(COMMUNITY_CHEST_CARD_POSITIONS + CHANCE_CARD_POSITIONS)
    card_transition[[card_positions, card_positions + 40, card_positions + 80]] = 0  # Card positions

    for transition in TRANSITION_CARD:
        for (current_state, next_state, proba) in transition:
            card_transition[to(*current_state), to(*next_state)] += proba

    for i in range(120):
        if not np.isclose(np.sum(dice_transition[i, :]), 1):
            print(i, np.sum(dice_transition[i, :]), dice_transition[i, :])
            assert False

    res = dice_transition @ card_transition
    np.savetxt("matrix.csv", res, delimiter=",", fmt="%f")

    for i in range(120):
        if not np.isclose(np.sum(res[i, :]), 1):
            print(i, np.sum(res[i, :]), res[i, :])
            assert False

    return res


def monopoly_odds():
    markov = get_markov()

    markov2 = np.linalg.matrix_power(markov, 100)
    proba = markov2[0, :]
    probability = proba[0:40] + proba[40:80] + proba[80:120]
    probability[10] += probability[30]
    probability[30] = 0
    print(sum(probability))
    print(np.sort(probability))
    print(np.argsort(probability))


if __name__ == "__main__":
    matrix = monopoly_odds()

    # np.savetxt("matrix.csv", matrix, delimiter=",", fmt="%f")
