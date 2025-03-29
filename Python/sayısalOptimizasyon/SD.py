import numpy as np
import math

def f(x):
    f = 3 + (x[0] - 1.5*x[1])**2 + (x[1]-2)**2
    return f

def gradf(x):
    gradf = np.array([2*(x[0]-1.5*x[1]), -3*(x[0]-1.5*x[1]) +2*(x[1]-2)])
    return gradf

def GSmain(f,xk,pk):
    xalt = 1
    xust = 1
    dx = 0.00001
    alpha = (1+math.sqrt(5))/2
    tau = 1-1/alpha
    epsilon = dx/(xust-xalt)
    N = round (-2.0278*math.log(epsilon))
    
    k = 0
    x1 = xalt + tau*(xust-xalt); f1 = f(xk+x1*pk);
    x2 = xust - tau*(xust - xalt); f2 = f(xk+x2*pk);
    
    for k in range(0,N):
        if f1>f2:
            xalt = 1*x1; x1 = 1*x2; f1= 1*f2;
            x2 = xust -tau(xust-xalt); f2 = f(xk+x2*pk);
        else:
            xust = 1*x2; x2 = 1*x1; f2 =1*f1;
            x1 = xalt + tau(xust-xalt); f1 = f(xk+x1*pk);
    x= 0.5*(x1+x2)
    return x
#----------------
#----------------ADIM1
x = np.array([-5.4 , 1.7])
X1 = [x[0]]
X2 = [x[1]]
Nmax = 10000
eps1 = 1e-10
eps2 = 1e-10
eps3 = 1e-10

k = 0

#--------------
updatex = np.array([1e10 , 1e10])
C1 = Nmax < k
C2 = abs(f(updatex) - f(x)) < eps1
C3 = np.linalg.norm(updatex -x) < eps2
C4 = np.linalg.norm(gradf(updatex)) < eps3
#-----ADIM3---*/.işğüüüüüüüüüüüüüüüüüüüüüüüüüü-*----*****-*-*
while not (C1 or C2 or C3 or C4):
    k+=1
    pk = -gradf(x) 
    sk= GSmain(f, x, pk) 
    x = x + sk*pk
    print("k:",k,"sk:" , round(sk,4), "x1:",round(x[0],4) , "x2:" ,round(x[1],4), "f:",round(f(x),4), "||gradf||:",round(gradf(x),4)) 
    C1 = Nmax < k
    C2 = abs(f(updatex) - f(x)) < eps1
    C3 = np.linalg.norm(updatex -x) < eps2
    C4 = np.linalg.norm(gradf(updatex)) < eps3    
    updatex = 1*x
    X1.append(x[0])
    X2.append(x[1])
    
if C1:
    print("...max . iterasyon sayısı aşıldı")
if C2:
    print(".. fonksiyon değişiyor")
if C3 :
    print("...değişkenler değişmiyor")
if C4:
    print("durağan noktaya gelindi")
    
#--------PLOT
import matplotlib.pyplot as plt
plt.plot(X1,X2)
plt.scatter(X1,X2,s=5, C='red')
plt.show()               
