import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt, mpld3
import pandas as pd
import os, sys
import math

" CONST "
DATA_DIR = os.path.join( os.path.dirname( __file__ ), '..\\', 'static\\data' )
A = -4
B = 4
STEP = 0.1
if (len(sys.argv)-1 > 0):
    try:
        N = int(sys.argv[1])
    except ValueError as e:
        N = 1000
else: N = 1000
WIDTH = 1600.0
HEIGHT = 900.0
FONTSIZE = 20.0

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

def first_plot(): 
    " First plot "
    default = pd.DataFrame({'x':values,
                        'f':first_default(values)})
    fourier = pd.DataFrame({'x':values,
                        'f':lambda_first_fourier(values)})
    plt.figure(figsize=(WIDTH/40,HEIGHT/40))
    if ('-show' not in sys.argv): 
        fig = plt.subplots()
    sns.lineplot(data=default, x="x", y="f", linewidth = 2)
    sns.lineplot(data=fourier, x="x", y="f", linewidth = 2)
    plt.legend(labels=['Default', 'Fourier'])
    if ('-show' not in sys.argv): 
        plt.savefig(f"{DATA_DIR}\\plot1.png", dpi = 300)
        mpld3.save_html(fig[0], f"{DATA_DIR}\\plot1.html")
    else: 
        plt.show()
def second_plot():
    " Second plot "
    default = pd.DataFrame({'x':values,
                        'f':second_default(values)})
    fourier = pd.DataFrame({'x':values,
                        'f':lambda_second_fourier(values)})
    plt.figure(figsize=(WIDTH/40,HEIGHT/40))
    if ('-show' not in sys.argv): 
        fig = plt.subplots()
    sns.lineplot(data=default, x="x", y="f", linewidth = 2)
    sns.lineplot(data=fourier, x="x", y="f", linewidth = 2)
    plt.legend(labels=['Default', 'Fourier'])
    if ('-show' not in sys.argv): 
        plt.savefig(f"{DATA_DIR}\\plot2.png", dpi = 300)
        mpld3.save_html(fig[0], f"{DATA_DIR}\\plot2.html")
    else: 
        plt.show()

def third_plot():
    " Third plot "
    default = pd.DataFrame({'x':values,
                        'f':third_default(values)})
    fourier = pd.DataFrame({'x':values,
                        'f':lambda_third_fourier(values)})
    plt.figure(figsize=(WIDTH/40,HEIGHT/40))
    if ('-show' not in sys.argv): 
        fig = plt.subplots()
    sns.lineplot(data=default, x="x", y="f", linewidth = 2)
    sns.lineplot(data=fourier, x="x", y="f", linewidth = 2)
    plt.legend(labels=['Default', 'Fourier'])
    if ('-show' not in sys.argv): 
        plt.savefig(f"{DATA_DIR}\\plot3.png", dpi = 300)
        mpld3.save_html(fig[0], f"{DATA_DIR}\\plot3.html")
    else: 
        plt.show()

def parse_html(): 
    for i in range(1, 4):
        file = open(f"{DATA_DIR}\\plot{i}.html", "r")
        new_file = file.read()
        file.close()
        file = open(f"{DATA_DIR}\\plot{i}.html", "w")
        new_file = __replace(new_file)
        file.write(new_file)

def __replace(new_file): 
    new_file = new_file.replace('11.0', f'{FONTSIZE}')
    new_file = new_file.replace('12.0', f'{FONTSIZE+1}')
    new_file = new_file.replace('640.0', f'{WIDTH}')
    new_file = new_file.replace('480.0', f'{HEIGHT}')
    return new_file

if __name__ == "__main__":
    if "-first" in sys.argv:
        first_plot()
    elif "-second" in sys.argv:
        second_plot()
    elif "-third" in sys.argv: 
        third_plot()
    else:
        first_plot()
        second_plot()
        third_plot()
        parse_html()