#y=2*x^2+3x-5
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,10,0.1)
y= x**2 +3*x - 5
plt.plot(x,y)