# def AND(x1: int, x2: int) -> int:
#     w1, w2, that = 0.5, 0.5, 0.7
#     tmp = w1 * x1 + w2 * x2
#     if tmp >= that:
#         return 1
#     else:
#         return 0

import numpy as np


def AND(x1: int, x2: int) -> int:
    nyuryoku = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    balsas = -0.7
    answer = np.sum(nyuryoku * weight) + balsas
    if answer <= 0:
        return 0
    else:
        return 1


def NAND(x1: int, x2: int) -> int:
    nyuryoku = np.array([x1, x2])
    weight = np.array([-0.5, -0.5])
    balsas = +0.7
    answer = np.sum(nyuryoku * weight) + balsas
    if answer <= 0:
        return 0
    else:
        return 1


def OR(x1: int, x2: int) -> int:
    nyuryoku = np.array([x1, x2])
    weight = np.array([0.5, 0.5])
    balsas = +0
    answer = np.sum(nyuryoku * weight) + balsas
    if answer <= 0:
        return 0
    else:
        return 1


print(NAND(0, 0))
print(NAND(0, 1))
print(NAND(1, 0))
print(NAND(1, 1))
