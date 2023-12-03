import numpy
import numpy as np

zeros = numpy.zeros
FLOAT = numpy.float64
dot = numpy.dot

# Number sides for each die
NUM_SIDES = 6

names = ("GO A1 CC1 A2 T1 R1 B1 CH1 B2 B3 "
         "JAIL C1 U1 C2 C3 R2 D1 CC2 D2 D3 "
         "FP E1 CH2 E2 E3 R3 F1 F2 U2 F3 "
         "G2J G1 G2 CC3 G3 R4 CH3 H1 T2 H2").split()
def FIND(tiles):
    return [names.index(name) for name in tiles.split()]
INDEX = names.index

cc = FIND("CC1 CC2 CC3")
ch1, ch2, ch3 = ch = FIND("CH1 CH2 CH3")
go = INDEX("GO")
jail = INDEX("JAIL")
g2j = INDEX("G2J")
c1 = INDEX("C1")
e3 = INDEX("E3")
h2 = INDEX("H2")
r1 = INDEX("R1")
r2 = INDEX("R2")
r3 = INDEX("R3")
u1, u2 = FIND("U1 U2")

#
dice = {}
for i in range(1, NUM_SIDES+1):
    for j in range(1, NUM_SIDES+1):
        dice[i+j] = dice.get(i+j, 0) + 1

TOT_DICE = sum(dice.values()) + 0.0

# The transition matrix is 120*120 in size.  The board is only
# 40*40 but there's hidden state for the doubles counter.
# The range 40:80 is if the 0:40 state rolled a double, and the
# 80:120 is for when a double is rolled while in 40:80.
transitions = zeros( (3*40, 3*40), FLOAT)

# I experimented with code to reset the doubles counter if sent to
# jail, but that doesn't match the 6-sided answers and the rules say
# there's no discinction between being on JAIL and being sent to jail.

def edge(old, new, advance, numerator, denominator):
    # "advance" is the value rolled; check to see if it could be a double
    count = dice[advance]
    if advance % 2 == 0:
        # one of these is a double; figure possibilities for all 3 copies
        p_normal = (count-1) * numerator / TOT_DICE / denominator
        p_double =             numerator / TOT_DICE / denominator
        transitions[old, new] += p_normal
        transitions[old, new+40] += p_double
        transitions[old+40, new] += p_normal
        transitions[old+40, new+80] += p_double
        transitions[old+80, new] += p_normal
        transitions[old+80, jail] += p_double
    else:
        # This is not a double, so everything goes back to the first copy
        p = count * numerator / TOT_DICE / denominator
        transitions[old, new] += p
        transitions[old+40, new] += p
        transitions[old+80, new] += p

# For each cell position; figure each possible die roll
for position in range(40):
    for advance in dice:
        # Might move to here, or not if the tile is special
        new_position = (position + advance) % 40

        if new_position == g2j: # Go to jail
            edge(position, jail, advance, 1, 1)

        elif new_position in cc:  # Community chest
            edge(position, new_position, advance, 14, 16)
        #     edge(position, go, advance, 1, 16)
        #     edge(position, jail, advance, 1, 16)
        #
        # elif new_position in ch:   # Chance
        #     edge(position, new_position, advance, 6, 16)
        #     for tile in [go, jail, c1, e3, h2, r1]:
        #         edge(position, tile, advance, 1, 16)
        #     if new_position == ch1:
        #         edge(position, r2, advance, 2, 16)
        #         edge(position, u1, advance, 1, 16)
        #         edge(position, new_position-3, advance, 1, 16)
        #     elif new_position == ch2:
        #         edge(position, r3, advance, 2, 16)
        #         edge(position, u2, advance, 1, 16)
        #         edge(position, new_position-3, advance, 1, 16)
        #     elif new_position == ch3:
        #         edge(position, r1, advance, 2, 16)
        #         edge(position, u1, advance, 1, 16)
        #         # There's a chance of backing up into the CC3, causing
        #         # another card to be drawn.  Include that effect.
        #         edge(position, new_position-3, advance, 1*14, 16*16)
        #         edge(position, go, advance, 1*1, 16*16)
        #         edge(position, jail, advance, 1*1, 16*16)
        else:
            # moved to a regular tile
            edge(position, new_position, advance, 1, 1)

# Start at "go" and iterate a couple hundred times
board = zeros( (3*40,), FLOAT )
board[0] = 1
np.savetxt("transitions.csv", transitions, delimiter=",", fmt="%f")
for i in range(200):  # don't really need this many iterations
    board = dot(board, transitions)

# Merge the three copies into one
output = zeros( (40,), FLOAT)
output[:] = board[0:40]
output[:] += board[40:80]
output[:] += board[80:120]

for prob, i in sorted((prob, i) for (i, prob) in enumerate(output)):
    print(i, names[i], prob)

# Last few are:
# 25 R3 0.0311078110187
# 16 D1 0.0322719757155
# 24 E3 0.0328820797844
# 15 R2 0.0361657166627
# 10 JAIL 0.0702255156635

# 101524