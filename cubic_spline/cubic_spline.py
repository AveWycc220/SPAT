import math
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

""" CONST """
WIDTH = 12
HEIGHT = 8

f = lambda x: x * (math.e ** -x)


def sweep(N, a=None, b=None, c=None, d=None, output_acc=False):
    if not a:
        a = [random.randint(0, 100) for i in range(N)]
    if not d:
        d = [random.randint(0, 100) for i in range(N)]
    if not b:
        b = [random.randint(0, 100) for i in range(N)]
    if not c:
        c = [random.randint(0, 100) for i in range(N)]
    c[0] = 0
    b[N-1] = 0
    u = [0 for i in range(N)]
    v = [0 for i in range(N)]
    y = [0 for i in range(N)]
    v[0] = -1 * b[0]/a[0]
    u[0] = d[0]/a[0]
    for i in range(1, N):
        u[i] = (d[i] - c[i]*u[i-1])/(c[i]*v[i-1]+a[i])
        v[i] = (-b[i])/(c[i]*v[i-1]+a[i])
    y[N-1] = u[N-1]
    for i in range(N-2, -1, -1):
        y[i] = u[i] + v[i]*y[i+1]
    if output_acc:
        print('---Accuracy---')
        for i in range(1, N-1):
            print(c[i]*y[i-1] + a[i]*y[i]+b[i]*y[i+1]-d[i])
    return y


def cubic_spline_m(h):
    N = int(10/h)
    x = [i*h for i in range(N)]
    fx = [f(x[i]) for i in range(N)]
    a = [4 for i in range(N)]
    b = [1 for i in range(N)]
    c = [1 for i in range(N)]
    d = [3*((fx[i+1]-fx[i-1])/h) for i in range(N-1)]
    d.append(0)
    a[0] = 1
    b[0] = 0
    c[0] = 0
    a[N-1] = 1
    b[N-1] = 0
    c[N-1] = 0
    d[0] = (fx[1] - fx[0])/h
    d[N-1] = (fx[N-1] - fx[N-2])/h
    m = sweep(N, a, b, c, d)
    y_spline = []
    x_s = [0.1 * i*h for i in range(10*(N-1))]
    for i in range(0, 10*(N-1)):
        j = math.floor((x_s[i]-x[0])/h)
        t = (x_s[i] - x[j])/h
        y_spline.append(fx[j]*((t-1) ** 2) * (2*t+1) + fx[j+1]*(t**2)*(3-2*t) + m[j]*h*t*((1-t) ** 2) - m[j+1]*h*(t**2)*(1-t))
    x_spline = [i*h for i in range(N-1)]
    x_function = np.arange(0, 11, 0.001)
    y_check = [f(x_function[i]) for i in range(len(x_function))]
    sns.set()
    plt.figure(figsize=(WIDTH, HEIGHT))
    plt.plot(x_s, y_spline, color='red')
    plt.plot(x_function, y_check, color='green')
    plt.title('Cubic Spline')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['Spline', 'Function'])
    plt.show()

def cubic_spline_M(h):
    N = int(10/h)
    x = [i*h for i in range(N)]
    fx = [f(x[i]) for i in range(N)]
    a = [4 for i in range(N)]
    b = [1 for i in range(N)]
    c = [1 for i in range(N)]
    d = [6*(fx[i+1]+fx[i-1]-2*fx[i])/(h ** 2) for i in range(N-1)]
    d.append(0)
    a[0] = 1
    b[0] = 0
    c[0] = 0
    a[N-1] = 1
    b[N-1] = 0
    c[N-1] = 0
    d[0] = (fx[0] + fx[2] - 2 * fx[1])/(h ** 2)
    d[N-1] = (fx[N-3] + fx[N-1] - 2 * fx[N-2])/(h ** 2)
    M = sweep(N, a, b, c, d)
    y_spline = []
    x_s = [0.1 * i*h for i in range(10*(N-1))]
    for i in range(0, 10*(N-1)):
        j = math.floor((x_s[i]-x[0])/h)
        t = (x_s[i] - x[j])/h
        y_spline.append(fx[j]*(1-t) + fx[j+1]*t +
                        M[j]*(h ** 2)*(t*(t-1)*(t-2) * -(1/6)) + M[j+1]*(h ** 2)*(t*(t-1)*(t+1) * (1/6)))
    x_spline = [i*h for i in range(N-1)]
    x_function = np.arange(0, 11, 0.001)
    y_check = [f(x_function[i]) for i in range(len(x_function))]
    sns.set()
    plt.figure(figsize=(WIDTH, HEIGHT))
    plt.plot(x_s, y_spline, color='red')
    plt.plot(x_function, y_check, color='green')
    plt.title('Cubic Spline')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['Spline', 'Function'])
    plt.show()


if __name__ == '__main__':
    cubic_spline_m(1)
    cubic_spline_M(1)