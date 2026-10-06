#SciPy: Scientific python
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.linspace(0, 10, 8)
y = np.sin(x)

func = interpolate.interp1d(x, y, kind='cubic')

x_interp = np.linspace(0, 10, 1000)
y_interp = func(x_interp)

plt.figure()
plt.plot(x, y, 'o')
plt.plot(x_interp, y_interp)

plt.show()