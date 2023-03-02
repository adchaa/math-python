import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*x + 2*x - 1
def g(x):
    return (1-x**2)*0.5

EPSILON = 10**-5 
Xa = 2
Xb = g(Xa)
n=1
print("n= ",n,"Xn = ",Xa,"Xn+1 = ",Xb)
while abs(Xa - Xb)> EPSILON :
    Xa = Xb
    Xb = g(Xa)
    n+=1
    print("n= ",n,"Xn = ",Xa,"Xn+1 = ",Xb)

# courbe 
X = np.arange(-2,2,0.001)
fx = f(X)
gx = g(X)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X,fx)
plt.plot(X,gx)
plt.plot(X,X)
plt.plot([Xa,Xa],[-2,5], '--')
plt.show()