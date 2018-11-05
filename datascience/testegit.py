import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(-np.pi, np.pi, 201)
y = np.sin(x)

plt.figure()
plt.plot(x,y)
plt.show()