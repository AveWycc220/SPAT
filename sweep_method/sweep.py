import random
import math
import seaborn as sns
import matplotlib.pyplot as plt

""" CONST """
WIDTH = 12
HEIGHT = 8


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


def boundary_value_problem(h):
    if 1 < h < 0:
        return 0
    N = int(1/h)
    x = [i*h for i in range(N)]
    check = lambda x_check: (math.sinh(x_check)/math.sinh(1)) - 2*x_check
    a = [-2 - (h ** 2) for i in range(N)]
    b = [1 for i in range(N)]
    c = [1 for i in range(N)]
    d = [2 * x[i] * (h ** 2) for i in range(N)]
    y = [0 for i in range(N)]
    y[0] = 0
    y[N-1] = -1
    a[0] = 1
    b[0] = 0
    c[0] = 0
    a[N-1] = 1
    c[N-1] = 0
    b[N-1] = 0
    d[0] = 0
    d[N-1] = -1
    y_sweep = sweep(N, a, b, c, d)
    y_check = [check(x[i]) for i in range(N)]
    sns.set()
    plt.figure(figsize=(WIDTH, HEIGHT))
    plt.plot(x, y_sweep, color='red')
    plt.plot(x, y_check, color='green')
    plt.title('Boundary Value Problem')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['Sweep', 'Correct'])
    plt.show()


if __name__ == '__main__':
    sweep(10, output_acc=False)
    boundary_value_problem(0.01)
