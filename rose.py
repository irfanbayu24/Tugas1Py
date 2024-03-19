import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 100)
x = np.sin(t) * np.sin(5 * t)
y = np.cos(t) * np.sin(5 * t)
z = np.cos(5 * t)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
plt.show()
