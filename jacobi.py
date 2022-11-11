def jacobi (A,B,x0,tol,n):
    D=np.diagflat(np.diag(A))
    LU=A-D
    x=x0
    for i in range(n):
        D_inv=np.linalg.inv(D)
        xtemp=x
        x=np.dot(D_inv,np.dot(-LU,x))+np.dot(D_inv,B)
        print("Iteración",i+1,":",x)
        if np.linalg.norm(x-xtemp)<tol:
            return x
    return x
import numpy as np
m=int(input("Ingrese el número ecuaciones: "))
n=int(input("Ingrese el número de coeficientes: "))
A=np.zeros((m,m))
x0=np.zeros(m)
b=np.zeros(m)
for r in range(0,m):
    for c in range(0,n):
        A[r][c]=float(input("Introduzca el coeficiente "+str(c+1)+" para la ecuación número "+str(r+1)+": "))
    b[(r)]=float(input("Introduzca la solución para la ecuación número "+str(r+1)+": "))
tol=float(input("Ingrese el valor de la tolerancia: "))
it=int(input("Ingrese el número de iteraciones: "))
x=jacobi(A,b,x0,tol,it)
