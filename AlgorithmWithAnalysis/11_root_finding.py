import numpy as np

def f(x):
     return x*np.exp(-x) + 1.0

def df(x):
    return np.exp(-x) - x*np.exp(-x)


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
    print(f'이분법 = {c:0.4f}')

# 가위치법
def false_position(a, b, n, f):
    a0 = a
    b0 = b
    c = (a0*f(b0) - b0*f(a0))/(f(b0) - f(a0))
    for i in range(n):
        if f(a0)*f(c) < 0:
            b0 = c
        else:
            a0 = c
        c = (a0*f(b0) - b0*f(a0))/(f(b0) - f(a0))
    print(f'가위치법 = {c:0.4f}')


# NR법
def newtonRhapson(n ,xo, f, df):
    xold = xo
    for k in range(n):
        xnew = xold - f(xold)/df(xold)
        xold = xnew
    print(f'뉴턴랩슨법 = {xnew:0.4f}')

# Secant법
def secant(n, xo, xm, f):
    xold = xo
    xmid = xm
    for k in range(n):
        xnew = xmid - f(xmid) * (xmid - xold)/(f(xmid) - f(xold))
        xold = xmid
        xmid = xnew
    print(f"할선법(secant) = {xnew:0.4f}")

bisection(-1, 1, 10, f)
false_position(-1, 1, 10, f)
newtonRhapson(10, 0, f, df)
secant(10, 0, 0.3, f)

"""
11근구하기
    11.1 구간법(Braking) : 근이 있을 가능성이 있는 구간을 정해놓고 구간내에서 근을 찾아내는 방식
        11.1.1 이분법
        11.1.2 가위치법
    11.2 반복법(Iterative) : 초기값을 주고 반복적인 과정을 통해서 근을 구하는 방식
        11.2.1 Newton법
        11.2.2 Secant법 : 뉴턴법이 도함수를 알아야한다는 점에서 수치미분 근사식 적용

이분법과 가위치법은 사전에 방정식 부호의 변화를 찾아야 한다는 어려움 존재
방정식의 부호의 변화가 없는 구간, 즉, 근이 없을 가능성이 높은 구간을 설정하면 근 구하기에 실패할 수 있다.

뉴턴방법은 빠른 수렴속도와 구간 설정에 얽매이지 않는다는 장점으로 가장 널리 쓰인다.
하지만 미분을 수행해야한다는 단점 존재, 적절치 못한 초기값으로 시작하면 수렴이 매우 느리거나 발산하는 경우도 존재
그러나 다변수, 비선형 문제에까지 확장가능하기에 다양하게 응용

할선법도 대체적으로 좋은 수렴속도를 보이지만, 방정식의 형태에 따라 두개 초기값에 따라 민감하게 반응하기도 함
모든 경우에 있어서 어떤 방법이 최고의 성능을 가지는 가를 가늠하는 것보다
방정식의 형태에 따라 적절한 방법을 적용하는 것을 경험하는 것이 더 중요

"""

