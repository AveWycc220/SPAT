import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

" CONST "
PATH = "F://Projects//SPAT//dft//"

def read_file(number_signal=1, N = 0):
    """ Read Signal from File """
    signal = []
    with open(PATH + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                    signal.append(int(values_list[number_signal-1]))
            if len(signal) == N and N != 0: 
                return signal
    return signal

def dft(signal, N):
    """ Default DFT """
    h = (2 * np.pi) / N
    divided_n = 1/np.sqrt(N)
    re = [0 for i in range(N)]
    for k in range(0, N):
        for m in range(0, N):
            re[k] += signal[m] * np.cos(h * k * m)
        re[k] *= divided_n
    im = [0 for i in range(N)]
    for k in range(0, N):
        for m in range(0, N):
            im[k] += signal[m] * np.sin(h * k * m)
        im[k] *= -divided_n
    result = [0 for i in range(N)]
    for i in range(0, N):
        result[i] = complex(re[i], im[i])
    return result

def parseval(signal, dft_signal, N, round = 0):
    """ Check for property of Parseval """
    print('-----Parseval-----')
    left = 0
    right = 0
    for m in range(0, N):
        left += ((dft_signal[m].real ** 2) + (dft_signal[m].imag ** 2))
    for k in range(0, N):
        right += (signal[k] ** 2)
    print(f'Fk = {left}')
    print(f'Fm = {right}')
    print(f'Difference = {np.abs(left-right)}')
    __print_percent(left, right, round)
    return right, left

def dft_convolution(f_signal, g_signal, N, round=0): 
    """ DFT on Convolution """
    h_signal = [0 for i in range(N)]
    for k in range (0, N):
        for m in range(0, N):
            if k < m:
                h_signal[k] += f_signal[k-m+N] * g_signal[m]
            else:
                h_signal[k] += f_signal[k-m] * g_signal[m]
    dft_h_signal = dft(h_signal, len(h_signal))
    dft_f_signal = dft(f_signal, len(f_signal))
    dft_g_signal = dft(g_signal, len(g_signal))
    print('-----Checking DFT on Convolution-----')
    right = 0
    left = 0
    for k in range(0, len(h_signal)):
        right += (np.abs(dft_h_signal[k]))
    for k in range(0, N):
        left += (np.abs(dft_f_signal[k])) * (np.abs(dft_g_signal[k]))
    left *= np.sqrt(N)
    print(f'Left = {left}')
    print(f'Right = {right}')
    print(f'Difference = {np.abs(left-right)}')
    __print_percent(left, right, round)
    return right, left

def __print_percent(left, right, round):
    if right > left: 
        if round != 0:
            print(f'{np.round(np.abs(left/right * 100 - 100), round)}%')
        else:
            print(f'{np.abs(left/right * 100 - 100)}%')
    else: 
        if round != 0:
            print(f'{np.round(np.abs(right/left * 100 - 100), round)}%')
        else:
            print(f'{np.abs(right/left * 100 - 100)}%')


if __name__ == "__main__":
    signal = read_file(1)
    N = len(signal)
    x = [i for i in range(N)]
    dft_signal = dft(signal, N)
    parseval(signal, dft_signal, N)
    second_signal = read_file(2)
    dft_convolution(signal, second_signal, N)
