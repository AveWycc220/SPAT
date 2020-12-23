import os
import math

""" CONSTS """
PATH = os.path.dirname(os.path.abspath(__file__)) + '\\'


def read_file(N):
    try:
        elem_list = []
        with open(PATH + f'D{N}.txt') as file:
            for elem in file.read().split('\n'):
                elem_list.append(float(elem))
        return elem_list
    except FileNotFoundError:
        print('Wrong N')
        return False


def check_sqrt(h):
    h_sum = sum(h)
    res = math.fabs(h_sum - math.sqrt(2))
    print(f'h_k - sqrt(2) = {res}')
    return res


def check_delta(h, N):
    h[len(h):] = [0 for _ in range(2 * N - 2)]
    res = []
    for m in range(0, N):
        temp = 0
        for k in range(0, 2 * N):
            temp += (h[k] * h[k+2*m])
        res.append(temp)
    print(f'Check Delta = {res}')
    return res


def check(N=2):
    coef = read_file(N)
    if coef:
        print(f'For N = {N}')
        check_sqrt(coef)
        check_delta(coef, N)
