import matplotlib.pyplot as plt
import numpy as np

num_values = 100

x = list(range(-1*num_values, num_values+1))
x.remove(0)

y = [i**(1/i) for i in x]
y = [np.sqrt(i.real**2+i.imag**2) if type(i) == complex else i for i in y ]

plt.plot(x, y)
plt.show()


