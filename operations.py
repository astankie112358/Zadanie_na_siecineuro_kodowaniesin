import numpy as np


def convertion(array: np.array, numberofgenerated: int):
    xlist = []
    for i in range(numberofgenerated):
        helpx = np.modf(array.take(i))
        integral = str(np.binary_repr(int(helpx[1])))
        for j in range(3 - len(integral)):
            integral = '0' + integral
        fractional = str(np.binary_repr(int(helpx[0] * 10000)))
        for j in range(14 - len(fractional)):
            fractional = '0' + fractional
        xlist.append(integral + fractional)
    return xlist


def make_spaceboard(string: str):
    string1 = string[0]
    for i in range(len(string) - 1):
        string1 = string1 + ' ' + string[i + 1]
    return string1
