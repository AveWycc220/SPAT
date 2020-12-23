import os
import math
import matplotlib.pyplot as plt

""" CONSTS """
PATH = os.path.dirname(os.path.abspath(__file__)) + '\\'


def read_file(number_signal=1, J=4):
    signal = []
    with open(PATH + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                signal.append(int(values_list[number_signal-1]))
    if 2 ** J > len(signal):
        return False
    return signal[:2 ** J]


def haar(M):
    J = int(math.ceil(math.log2(M)))
    M = 2 ** J
    signal = read_file(1, J)
    if signal:
        S = [[0 for _ in range(M)] for _ in range(J + 1)]
        d = [[0 for _ in range(M)] for _ in range(J + 1)]
        S[0] = signal[:]
        for j in range(J):
            for m in range(int(M/(2 ** (j+1)))):
                S[j+1][m] = (S[j][2*m] + S[j][2*m+1]) / math.sqrt(2)
                d[j+1][m] = (S[j][2*m] - S[j][2*m+1]) / math.sqrt(2)
        check_right = 0
        for i in range(M):
            check_right += (S[0][i] ** 2)
        check_left = 0
        for j in range(J+1):
            for m in range(M):
                check_left += (d[j][m] ** 2)
        print(f'Difference = {check_right - (check_left + (S[J][0] ** 2))}')
        for j in range(J-1, -1, -1):
            for m in range(int(M/(2 ** j))):
                S[j][m] = (S[j+1][int(m/2)] + ((-1) ** m)*d[j+1][int(m/2)]) / math.sqrt(2)
        x = [i for i in range(M)]
        plt.figure()
        plt.plot(x, signal, color='red')
        plt.plot(x, S[0], color='green')
        plt.legend(['Signal', 'S[0]'])
        plt.show()


if __name__ == '__main__':
    haar(5)
