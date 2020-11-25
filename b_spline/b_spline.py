import math
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.signal as signal

""" CONST """
WIDTH = 12
HEIGHT = 8

""" Lambda """
b_first = lambda x: 1 if 0.5 > x >= -0.5 else 0
b_n_first = lambda x: 1 if 0.5 >= x >= -0.5 else 0
b_n = lambda x, n: b_first(x) if n == 1 else (n+2*x)/(2*(n-1))*b_n(x+0.5, n-1)+(n-2*x)/(2*(n-1))*b_n(x-0.5, n-1)


def beta_spline(n, h=1.0):
    if n < 1:
        return None
    n_b = n+1
    n = (n+1)/h
    b = [0 for _ in np.arange(-1 * n / 2, (n / 2) + 0.5, 0.5)]
    x = [i * h for i in np.arange(-1 * n / 2, (n / 2) + 0.5, 0.5)]
    if n == 1:
        for i in range(0, len(x)):
            b[i] = b_n_first(x[i])
        return x, b
    for i in range(0, len(x)):
        b[i] = b_n(x[i], n_b)
    return x, b


if __name__ == '__main__':
    x_10, y_10 = beta_spline(10)
    x_15, y_15 = beta_spline(15)
    y_signal = signal.bspline(x_15, 15)
    sns.set()
    fig, axs = plt.subplots(2, figsize=(WIDTH, HEIGHT))
    axs[0].plot(x_10, y_10, color='red')
    axs[0].plot(x_15, y_15, color='green')
    axs[0].set_title('Beta Splines')
    axs[0].set_xlabel('X')
    axs[0].set_ylabel('Y')
    axs[0].legend(['Spline (n=10)', 'Spline (n=15)'])
    axs[1].plot(x_15, y_signal, color='black')
    axs[1].set_xlabel('X')
    axs[1].set_ylabel('Y')
    axs[1].legend(['Spline (scipy.signal, n=15)'])
    plt.show()