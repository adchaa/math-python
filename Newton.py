import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x**2)-4*x**2
def derive_f(x):
    return 2*x*np.exp(x**2)-8*x
def newton(x0):
    print('------------------------------------------------------------------')
    n=1
    Xa = x0
    if(derive_f(Xa) != 0):
        Xb= Xa - f(Xa)/derive_f(Xa)
    print("n= ",n,"Xn = ",Xa,"Xn+1 = ",Xb)
    while abs(Xa - Xb)> EPSILON:
        Xa = Xb
        if(derive_f(Xa) !=0):
            Xb= Xa - f(Xa)/derive_f(Xa)
        n+=1
        print("n= ",n,"Xn = ",Xa,"Xn+1 = ",Xb)
    return Xa
EPSILON = 10**-10
result1 = newton(-1)
result2 = newton(-1.5)
result3 = newton(1)
result4 = newton(1.5)
X = np.arange(-1.5,1.5,0.001)
fx = f(X)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X,fx)
plt.plot(np.repeat(result1,2),[-1,2], '--')
plt.plot(np.repeat(result2,2),[-1,2], '--')
plt.plot(np.repeat(result3,2),[-1,2], '--')
plt.plot(np.repeat(result4,2),[-1,2], '--')
plt.show()