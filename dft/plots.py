import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

" CONST "
PATH = "F://Projects//SPAT//dft//"
WIDTH = 12
HEIGHT = 8
    
def read_file(number_signal=1):
    signal = []
    with open(PATH + 'openedEyes.asc') as file:
        for elem in file.read().split('\n'):
            values_list = elem.split(' ')
            if len(values_list) == 3:
                    signal.append(int(values_list[number_signal-1]))
    return signal

def dft(signal, N):
    h = (2 * np.pi) / N
    divided_n = 1/np.sqrt(N)
    re = [0 for i in range(N)]
    for k in range(0, N):
        for m in range(0, N-1):
            re[k] += signal[m] * np.cos(h * k * m)
        re[k] *= divided_n
    im = [0 for i in range(N)]
    for k in range(0, N):
        for m in range(0, N-1):
            im[k] += signal[m] * np.sin(h * k * m)
        im[k] *= -divided_n
    result = [0 for i in range(N)]
    for i in range(0, N):
        result[i] = complex(re[i], im[i])
    return result

def back_dft(signal, N):
    h = (2 * np.pi) / N
    divided_n = 1/np.sqrt(N)
    re = [signal[i].real for i in range(0, N)]
    im = [signal[i].imag for i in range(0, N)]
    fm = [0 for i in range(0, N)]
    for m in range(0, N):
        for k in range(0, N-1):
            fm[m] += (re[k]*np.cos(h * k * m) - im[k]*np.sin(h * k * m))
        fm[m] *= divided_n
    return fm

def remove_frequencies(signal, N, a, b):
    for i in range(0, N):
        if i > a and i < b:
            signal[i] = complex(0, 0)
    return signal

if __name__ == "__main__":
    signal = read_file(1)
    N = len(signal)
    x = [i for i in range(N)]
    sns.set()
    plt.figure(figsize=(WIDTH,HEIGHT))
    plt.plot(x, signal, color='red')
    plt.title('Before Fourier Transform')
    plt.legend(['Signal'])
    plt.xlabel('Time')
    plt.ylabel('Value of F(x)')
    plt.show()
    dft_signal = dft(signal, N)
    dft_signal = remove_frequencies(dft_signal, N, 150, 1150)
    plt.figure(figsize=(WIDTH,HEIGHT))
    plt.xlim(-50, 300)
    plt.ylabel('Value of F(x)')
    plt.xlabel('Hz')
    plt.plot(x, dft_signal, color='green')
    plt.title('After Fourier Transform')
    plt.legend(['DFT_Signal'])
    plt.show()
    back_dft_signal = back_dft(dft_signal, N)
    plt.figure(figsize=(WIDTH,HEIGHT))
    plt.title('Before Back Fourier Transform')
    plt.plot(x, signal, color='red')
    plt.plot(x, back_dft_signal, color='green')
    plt.legend(['Signal', 'Back_DFT_Signal'])
    plt.xlabel('Time')
    plt.ylabel('Value of F(x)')
    plt.show()