import numpy as np

x0 = 2
err = 1

while err>=10**-10:
    x = x0 - (x0**2-2)/(2*x0)
    err = np.abs(x0 - x)
    x0 = x
   
print(x0)