import numpy as np 
import matplotlib.pyplot as plt 

for i in range(4):
  data = np.loadtxt(str(i)+'.dat')
  plt.plot(data[0],data[1])
plt.xlabel('x')
plt.ylabel('u(x)')
plt.savefig('adveccion.pdf')
