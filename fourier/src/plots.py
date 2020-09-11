import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import os
import math

" CONST "
DATA_DIR = os.path.join( os.path.dirname( __file__ ), '..', 'data\\' )
A = -4
B = 4
STEP = 0.1
N = 10000

" Functions "
first_default = lambda x: x
def first_fourier(x):
    n = 1; total = 0
    while n < N:
        total += ((-1) ** (n+1) * math.sin(n * x)) / n
        n += 1
    return 2 * total
lambda_first_fourier = np.vectorize(first_fourier)
second_default = lambda x: x ** 2
def second_fourier(x):
    n = 1; total = 0
    while n < N:
        total += ((-1) ** (n) * math.cos(n * x)) / n ** 2
        n += 1
    return (math.pi ** 2)/3 + 4 * total
lambda_second_fourier = np.vectorize(second_fourier)
third_default = lambda x: np.sign(x)
def third_fourier(x):
    n = 1; total = 0
    while n < N:
        total += math.sin((2*n-1)*x)/(2*n-1)
        n += 1
    return (4/math.pi) * total
lambda_third_fourier = np.vectorize(third_fourier)

sns.set_theme()
" Created values "
values = np.arange(A, B, STEP, dtype=float)
" First plot "
default = pd.DataFrame({'x':values,
                       'f':first_default(values)})
fourier = pd.DataFrame({'x':values,
                       'f':lambda_first_fourier(values)})
plt.figure()
fig, ax = plt.subplots()
first_plot = sns.lineplot(data=default, x="x", y="f", linewidth = 2)
second_plot = sns.lineplot(data=fourier, x="x", y="f", linewidth = 2)
plt.legend(labels=['Default', 'Fourier'])
plt.savefig(f"{DATA_DIR}\\plot1.png")
mpld3.save_html(fig, f"{DATA_DIR}\\plot1.html")
" Second plot "
default = pd.DataFrame({'x':values,
                       'f':second_default(values)})
fourier = pd.DataFrame({'x':values,
                       'f':lambda_second_fourier(values)})
plt.figure()
fig, ax = plt.subplots()
first_plot = sns.lineplot(data=default, x="x", y="f", linewidth = 2)
second_plot = sns.lineplot(data=fourier, x="x", y="f", linewidth = 2)
plt.legend(labels=['Default', 'Fourier'])
plt.savefig(f"{DATA_DIR}\\plot2.png")
mpld3.save_html(fig, f"{DATA_DIR}\\plot2.html")
" Third plot "
default = pd.DataFrame({'x':values,
                       'f':third_default(values)})
fourier = pd.DataFrame({'x':values,
                       'f':lambda_third_fourier(values)})
plt.figure()
fig, ax = plt.subplots()
first_plot = sns.lineplot(data=default, x="x", y="f", linewidth = 2)
second_plot = sns.lineplot(data=fourier, x="x", y="f", linewidth = 2)
plt.legend(labels=['Default', 'Fourier'])
plt.savefig(f"{DATA_DIR}\\plot3.png")
mpld3.save_html(fig, f"{DATA_DIR}\\plot3.html")