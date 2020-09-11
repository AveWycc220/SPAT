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

first_default = lambda x: x
def first_fourier(x):
    n = 1; total = 0
    while n < N:
        total += ((-1) ** (n+1) * math.sin(n * x)) / n
        n += 1
    return 2 * total
lambda_first_fourier = np.vectorize(first_fourier)

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