from scaling_func import read_file
import os
import math
import matplotlib.pyplot as plt

""" CONSTS """
PATH = os.path.dirname(os.path.abspath(__file__)) + '\\'


def read_file_signal(number_signal=1, J=4):
    signal = []
    with open(PATH + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                signal.append(int(values_list[number_signal-1]))
    if 2 ** J > len(signal):
        return False
    return signal[:2 ** J]


def order_burst(M):
    J = int(math.ceil(math.log2(M)))
    signal = read_file_signal(1, J)
    h = read_file(2)
    if h and signal:
        J = int(math.ceil(math.log2(M)))
        M = 2 ** J
        n = len(h)
        S = [[0 for _ in range(M)] for _ in range(J + 1)]
        d = [[0 for _ in range(M)] for _ in range(J + 1)]
        S[0] = signal[:]
        for j in range(J):
            for l in range(int(M/(2 ** (j+1)))):
                for m in range(2*l, (2*l+n)):
                    if m < int(M/(2 ** j)):
                        S[j+1][l] += h[m-2*l]*S[j][m]
                    else:
                        S[j+1][l] += h[m-2*l]*S[j][m - int(M/(2 ** j))]
                for m in range(2 * l + 1 - (n-1), 2 * l + 2):
                    if m >= 0:
                        d[j+1][l] += ((-1) ** m) * h[1-m+2*l]*S[j][m]
                    else:
                        d[j+1][l] += ((-1) ** m) * h[1-m+2*l]*S[j][m + int(M/(2 ** j))]
        check_left = 0
        check_right = 0
        for m in range(M):
            check_left += (S[0][m] ** 2)
        for j in range(J + 1):
            for m in range(int(M/(2**j))):
                check_right += (d[j][m] ** 2)
        print(f'Difference = {check_left - (check_right + (S[J][0] ** 2))}')
        for j in range(J-1, -1, -1):
            for m in range(int(M/(2 ** j))):
                for l in range(math.ceil((m-(n-1))/2), math.floor(m/2)):
                    if l >= 0:
                        S[j][m] += h[m-2*l] * S[j+1][l]
                    else:
                        S[j][m] += h[m - 2 * l] * S[j+1][l + int(M/(2 ** (j+1)))]
                for l in range(math.ceil((m-1)/2), math.floor((m+n-2)/2)):
                    if l < int(M / (2 ** j)):
                        S[j][m] += ((-1) ** m) * h[1-m+2*l] * d[j+1][l]
                    else:
                        S[j][m] += ((-1) ** m) * h[1 - m + 2 * l] * d[j+1][l - int(M/(2 ** (j+1)))]
        x = [i for i in range(M)]
        plt.figure()
        plt.plot(x, signal, color='red')
        plt.plot(x, S[0], color='green')
        plt.legend(['Signal', 'S[0]'])
        plt.show()


if __name__ == '__main__':
    order_burst(100)