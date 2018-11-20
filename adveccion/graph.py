import numpy as np 
import matplotlib.pyplot as plt 

for i in range(4):
  data = np.loadtxt(str(i)+'.dat')
  plt.plot(data[0],data[1])
# plt.show()
plt.savefig('adveccion.pdf')
