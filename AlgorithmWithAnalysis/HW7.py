import numpy as np
from scipy.linalg import lu
import scipy.linalg
# 32190956 김은상 HW7
#
# 2차 보간 함수
def polynomInterp(x1, x2, x3, y1, y2, y3, at):
    beta0 = y1
    beta1 = (y2-y1)/(x2-x1)
    beta2 = ((y3-y2)/(x3-x2) - (y2-y1)/(x2-x1))/(x3-x1)
    return print(f'다항 보간법{beta0 + beta1*(at - x1) + beta2*(at - x1)*(at-x2)}')

# 사다리꼴 적분 함수
def trapezoid(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2*f(a + i*h)
    return print(f'사다리꼴 적분공식{h*s/2}')

def f_for_10_5_2(x):
    return x**3 + 1

def f_for_10_5_3(x):
    return x*np.cos(x)

def f_for_11_7_1(x):
     return x**4 - 8.0

def f_for_11_7_8(x):
    return x**2 + np.sin(x) - 0.1

def df_for_11_7_8(x):
    return 2*x + np.cos(x)

# 심슨 3/8 공식 함수
def simpsons_3_8_rule(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s += 2*f(a + i*h)
        else:
            s += 3*f(a + i*h)
    return print(f'심슨 3/8 적분공식{3 * h / 8 * s}')

# 이분법
def bisection(a, b, n, f):
    c = (a+b)/2.0
    for i in range(n):
        if f(a)*f(c) < 0:
            b = c
        elif f(c)*f(b) < 0:
            a = c
        else:
            print("No sign change")
    c = (a + b)/2.0
    print(f'이분법 c = {c:0.4f}')

# NR법
def newtonRhapson(a, b, n ,xold, f, df):
    xnew = 0.0
    for k in range(n):
        xnew = xold - f(xold)/df(xold)
        xold = xnew
    print(f'뉴턴랩슨법(근구하기) = {xnew:0.4f}')

#LU분해법
def luComposition(A, b):
    P, L, U = lu(A)
    return print(f'LU분해법 = {np.linalg.inv(A) @ (np.linalg.inv(L) @ b)}')

# 콜레스키 분해법
def cholesky(A, b):
    L = scipy.linalg.cholesky(A, lower=True)
    LT = L.T
    invLT = np.linalg.inv(LT)
    invL = np.linalg.inv(L)

    x = invLT @ (invL @ b)
    return print(f'콜레스키 분해법 = {x}')

# Jacobi 방법
def jacobi(A, b, n, xold):
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    D = np.diag(np.diag(A))

    former = np.linalg.inv(D) @ b

    for k in range(n):
        latter = - (np.linalg.inv(D) @ (L + U)) @ xold
        xnew = former + latter
        xold = xnew
    return print(f'자코비 방법 = {xnew}')

# 가우스 세이델 방법
def gaussSeidel(A, b, n, xold):
    L = np.tril(A,-1)
    U = np.triu(A,1)
    D = np.diag(np.diag(A))

    former = np.linalg.inv(L + D) 

    for k in range(n):
        latter = b - U @ xold
        xnew = former @ latter
        xold = xnew
    return print(f'가우스 세이델 방법 = {xnew}')

# 회귀법
def regression(x, y):
    n = len(x)

    beta0_nom = np.sum(y)*np.sum(x**2) - np.sum(x)*np.sum(x*y)
    denom = n*np.sum(x**2) - (np.sum(x))**2 
    beta0 = beta0_nom / denom

    beta1_nom = n*np.sum(x*y) - np.sum(x)*np.sum(y)
    beta1 = beta1_nom / denom

    yhat = beta0 + beta1 * x  
    print(f'회귀법으로 구한 yhat = beta0 + beta1 * x{yhat}')
    return print(f'회귀법으로 구한 베타값 -> beta0 = {beta0}, beta1 = {beta1}')

print("p160 - 4")
polynomInterp(1, 2, 3, 3, 6, 9, 1.7)
print("")
print("")
print("")
print("-------------------------------")
print("p160 - 5")
polynomInterp(1, 2, 3, 9, 2, 4, 1.8)
print("p182 - 2")
print("")
print("")
print("")
print("-------------------------------")
trapezoid(1, 2, 5, f_for_10_5_2)
print("p182 - 3")
print("")
print("")
print("")
print("-------------------------------")
simpsons_3_8_rule(0, 4, 6, f_for_10_5_3)
print("p203 - 1")
print("")
print("")
print("")
print("-------------------------------")
bisection(1, 5, 10, f_for_11_7_1)
print("p203 - 8")
print("")
print("")
print("")
print("-------------------------------")
newtonRhapson(0, 10, 10, 0, f_for_11_7_8, df_for_11_7_8)
print("p252 - 6")
print("")
print("")
print("")
print("-------------------------------")
luComposition(np.array([[9, -1, 1], [-1, 5, -1], [1, -1, 2]]), np.array([[4], [0], [9]]))
print("p252 - 9")
print("")
print("")
print("")
print("-------------------------------")
cholesky(np.array([[2, -1, 1], [-1, 3, -1], [1, -1, 2]]), np.array([[4], [6], [15]]))
print("p276 - 3")
print("")
print("")
print("")
print("-------------------------------")
jacobi(np.array([[7, 2, 1], [2, 8, 3], [1, 3, 6]]), np.array([[3], [2], [2]]), 10, np.array([[0], [0], [0]]))
print("p276 - 5")
print("")
print("")
print("")
print("-------------------------------")
gaussSeidel(np.array([[5, -1, 1], [-1, 7, 3], [1, 3, 6]]), np.array([1, 1, 5]).T, 10, np.array([0, 0, 0]).T)
print("p308 - 6")
print("")
print("")
print("")
print("-------------------------------")
regression(np.array([1, 2, 3, 4, 5]), np.array([10, 15, 13, 17, 21]))
print("p308 - 7")
print("")
print("")
print("")
print("-------------------------------")
regression(np.array([1, 2, 3, 4, 5]), np.array([8.5, 7, 6, 4.5, 3]))


