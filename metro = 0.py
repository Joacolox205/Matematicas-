#grafico.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def f(t):
    return 0.4*t
t = np.arange(0, 60, 2)
plt.plot(t, f(t))
plt.title('distancia recorrida por minutos en metro')
plt.ylabel('distancia (km)')
plt.xlabel('tiempo (minutos)')
plt.legend()
plt.grid()
plt.show()

