import numpy as np


def random_color(x):
    def prep(y):
        if hex(y)[2:] == 6:
            return "#" + hex(y)[2:]
        else:
            return "#" + "0" * (6 - len(hex(y)[2:])) + hex(y)[2:]
    b = np.random.randint(0,16777125,x)
    c = [(prep(c)) for c in b]
    return c

