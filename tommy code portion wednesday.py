score_square_centres = {
    1: (1700, 1700),
    2: (2700, 1700),
    3: (3700, 1700),
    4: (1700, 2700),
    5: (2700, 2700),
    6: (3700, 2700),
    7: (1700, 3700),
    8: (2700, 3700),
    9: (3700, 3700)
}
def what_score_square_am_i_in(x, z):
    if x < 1200 or z < 1200 or x > 4200 or z > 4200:
        return 0 # not in any square

    elif x < 2200:

        if z < 2200:
            return 1

        elif z < 3200:
            return 4

        else:
            return 7

    elif x < 3200:

        if z < 2200:
            return 2

        elif z < 3200:
            return 5

        else:
            return 8

    else:

        if z < 2200:
            return 3

        elif z < 3200:
            return 6

        else:
            return 9
