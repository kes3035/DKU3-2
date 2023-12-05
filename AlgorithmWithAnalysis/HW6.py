import numpy as np
import scipy as sp
# 11.7      3,5,7
# 12.6      1,6,13



def f(x):
    return np.cos(x) + x - 3

def f5(x):
    return x**2 + np.sin(x) - 0.1

def f7(x):
    return x**4 - 8

def df7(x):
    return 4*(x**3)

def bisection11_7_3():
    a = -3
    b = 5
    c = (a + b)/2.0

    for _ in range(20):
        if f(a)*f(b) < 0:
            b = c
        elif f(a)*f(c) < 0:
            a = c
        c = (a+b)/2.0
    print(f'연습문제 11.7의 3번 = {c:0.4f}')

def falsePosition11_7_5():
    a = 0
    b = 10
    c = (a*f5(b) - b*f5(a))/(f5(b) - f5(a))

    for _ in range(100):
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
        c = (a*f5(b) - b*f5(a))/(f5(b) - f5(a))
    print(f'연습문제 11.7의 5번 = {c:0.4f}')

def newtonRhapson11_7_7():
    xold = 1.5
    for _ in range(20):
        xnew = xold - f7(xold)/df7(xold)
        xold = xnew
    print(f'연습문제 11.7의 7번 = {xold:0.4f}')

bisection11_7_3()
falsePosition11_7_5()
newtonRhapson11_7_7()

A = np.array([[6, 3, 2], [3, 5, 1], [2, 1, 7]])
B = np.array([[3, 2], [3, 5]])

def solve12_6_1():
    b = np.array([[1, 3, 5], [2, 4, 6]])
    x = np.array([[10], [9], [8]])

    print(f'연습문제 12.6의 1번 = \n{b@x}')

def solve12_6_6():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    invA = np.linalg.inv(A)

    print(f'연습문제 12.6의 6번 = {A@invA}')

def solve12_6_13():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    C = np.array([5, 6, 7])
    transposedC = C.T
    print(f'연습문제 12.6의 13번 = {A@transposedC}')

solve12_6_1()
solve12_6_6()
solve12_6_13()