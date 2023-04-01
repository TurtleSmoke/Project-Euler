# Brute force

For once, this problem only requires implementation of poker rules and does not involve any mathematical or algorithmic concepts.
While the rules are straightforward, it can be tedious to implement due to the many possible outcomes.
It is important to understand how to compare two hands to write less verbose code and not avoid missing some outcomes.

The rules for comparing hands are as follows:

- The hand with the highest rank wins.
- If two hands have the same rank, the one with the highest card wins.
- If two hands have the same rank and the same highest card, the one with the second-highest card wins and so on.

There is a special case for the Full House rank, for example, the Full House `4D 4S 4H 2C 2D` is better than the Full House `3D 3S 3H 5C 5D` because the three fours are better than the three threes (even if the pair of fives is better than the pair of twos).
Therefore, the rank of the hand alone is not sufficient to compare two hands, it is also required to know the occurrences of each card rank.

There may be more tricky cases (depending on the poker variant), but this is enough to solve the problem.

The input file is read using `read_file` function which returns a simple list of all cards of both hands.

From [read_file.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0054/read_file.py):

```python
def read_file(filename):
    with open(filename, "r") as file:
        return [line.split() for line in file.read().splitlines()]
```

For convenience and readability, `Rank`, `Suit` and `Hand` enums are defined and the `from_string` function is used to parse the input strings into cards.

Then, three information are extracted from each hand:

- The list of cards (sorted by occurrence and rank).
- If the hand is straight (all cards have consecutive ranks).
- If the hand is flush (all cards have the same suit).

Creating a tuple with rank of the hand and the list of cards (sorted by occurrence and rank) is enough to compare two hands.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0054/solution1.py):

```python
def get_hand(hand):
    values = sorted([Card.from_string(card[0]) for card in hand])
    occ, values = zip(*sorted(((v, k) for k, v in Counter(values).items()), reverse=True))

    is_straight = all(values[i].value == values[i + 1].value + 1 for i in range(len(values) - 1))
    is_flush = len(set(card[1] for card in hand)) == 1

    if occ == (4, 1):
        hand = Hand.FOUR_OF_A_KIND
    elif occ == (3, 2):
        hand = Hand.FULL_HOUSE
    elif occ == (3, 1, 1):
        hand = Hand.THREE_OF_A_KIND
    elif occ == (2, 2, 1):
        hand = Hand.TWO_PAIR
    elif occ == (2, 1, 1, 1):
        hand = Hand.ONE_PAIR
    elif is_straight and is_flush and values[0] == Card.ACE:
        hand = Hand.ROYAL_FLUSH
    elif is_straight and is_flush:
        hand = Hand.STRAIGHT_FLUSH
    elif is_flush:
        hand = Hand.FLUSH
    elif is_straight:
        hand = Hand.STRAIGHT
    elif occ == (1, 1, 1, 1, 1):
        hand = Hand.HIGH_CARD
    else:
        raise ValueError("Invalid hand")

    return hand, *values
```

The rest is just a matter of iterating over all the hands and counting the number of wins for player 1.

From [solution1.py](https://github.com/TurtleSmoke/Project-Euler/blob/main/problems/problem_0054/solution1.py):

```python
def poker_hands(file):
    return sum(get_hand(hand[:5]) > get_hand(hand[5:]) for hand in read_file(file))
```
