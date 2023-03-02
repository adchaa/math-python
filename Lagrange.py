import numpy as np
import matplotlib.pyplot as plt
class Lagrange:
    def __init__(self,xi : list,yi : list) -> None:
        self.Xi = xi
        self.Yi = yi
        self.dev_Li = []
        self.init_dev_Li()

    def exclude(self,L : list,i):
        output = L.copy()
        output.pop(i)
        return output
        
    def prod(self,iterable):
        S = 1
        for x in iterable:
            S *= x
        return S
    # 1/value
    def init_dev_Li(self):
        for i in range(len(self.Xi)):
            temp = []
            for j in self.exclude(self.Xi,i):
                temp.append(self.Xi[i] - j)
            self.dev_Li.append(1/self.prod(temp))
    
    def calcul_Li(self,x,i):
        output = 1
        for j in self.exclude(self.Xi,i):
            output *= x-j
        return output*self.dev_Li[i]
    def calcul(self,x):
        p = 0
        for i in range(len(self.Xi)):
            p += self.Yi[i]*self.calcul_Li(x,i)
        return p
Xi = [0,1,-1,2]
Yi = [0.5,2,0,10.5]
P =Lagrange(Xi,Yi)

X = np.arange(-10,10,0.001)
Y = []
for i in X:
    Y.append(P.calcul(i))
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(X,Y)
plt.xlim(-10,10)
plt.ylim(-10,10)
#plt.plot(-1, P.calcul(-1), marker="D", markersize=5, markeredgecolor="red", markerfacecolor="green")
plt.show()
        