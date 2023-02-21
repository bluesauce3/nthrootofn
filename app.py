import matplotlib.pyplot as plt
import numpy as np

num_values = 100

x = list(range(-1*num_values, num_values+1))
x.remove(0)

y = [i**(1/i) for i in x]

plt.plot(x, y)
plt.show()


