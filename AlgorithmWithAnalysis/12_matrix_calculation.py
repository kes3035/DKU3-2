# 행렬연산
import numpy as np
"""
전치(transpose) => a.T
행렬식(determinant) => np.linalg.det(a)
역행렬(inversed) => np.linalg.inv(a)
"""


a = np.array([1,2,3])
b = np.array([4,5,6])
print(f'c = {a@b}')

print(f'c = {a@b.T}')

c = np.array([[1, 9, 99], [2, 8, 88], [3, 7, 77]])
print(f'c.T = \n{c.T}')


A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

N = 10
xold = np.array([0.0,0.0,0.0])

L = np.tril(A,-1)
U = np.triu(A,1)
D = np.diag(np.diag(A))

former = np.linalg.inv(D) @ b 

for k in range(N):
    latter = - (np.linalg.inv(D) @ (L+ U)) @ xold
    xnew = former + latter
    error = abs(xnew-xold)/xold * 100
    xold = xnew
    print(k+1, xnew, error)

