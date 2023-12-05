import numpy as np
from scipy import integrate
"""
수치적분
1. 사다리꼴 적분공식  ---| -> 보간법 응용
2. Simpson 적분공식 ---|
3. Gauss 구적법     ------> 가중값 공식
"""
"""
사다리꼴 적분공식이 정확도가 낮은 이유
선형보간법을 이용한 한계로 실 곡선을 따라가지 못함! 그래서 정확도가 낮음
이 한계를 극복? -> 보간법의 차수를 높인다
"""
def f(x):
    return x**2 * np.exp(-x)

def trapezoid(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2*f(a + i*h)
    return print(f'사다리꼴 적분공식{h*s/2}')

def simpsons_1_3_rule(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        if i%2 == 0:
            s += 2*f(a + i*h)
        else:
            s += 4*f(a + i*h)
    return print(f'심슨 1/3 적분공식{h / 3 * s}')

def simpsons_3_8_rule(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s += 2*f(a + i*h)
        else:
            s += 3*f(a + i*h)
    return print(f'심슨 3/8 적분공식{3 * h / 8 * s}')
# Simpson 적분공식 -> 사다리꼴 적분공식의 단점을 보완하기 위해 선형 보간법의 차수를 높인 것!
# 심슨의 1/3 공식
# 처음과 끝을 제외한 중간들의 x_i값들이 홀수일땐 앞에 4를, 짝수일땐 앞에 2를 곱한다

# 평균? -> 똑같은 가중치를 주고 계산하는 것

# 11.08 (W)
# 데이터를 사용한 적분
# 실험 데이터등을 사용하여 적분을 구해야하는 경우
# 예를 들어 자동차의 속도에 대해 적분을 하면 주행거리를 알 수 있다.
# 또, 미사일의 가속도를 통해 미사일의 속도를 알 수 있다.

# Gauss 구적법 ( Gaussian Quadrature )
## 특정 위치에서의 함수 값과 그에 해당하는 가중 값의 곱을 합산하여 근사적으로 적분을 계산하는 방법
## node : 절점, weight : 가중값
## 절점과 가중값을 알아야 사용가능
## 적분구간은 항상 -1부터 +1 까지

area, error = integrate.quad(f, a, b)



f = lambda x: x**2
a, b = 0, 1
x = np.linspace(a, b, num = 100)
y = f(x)

area_np = np.trapz(y, x)
area_sp = integrate.trapz(y, x)
area = integrate.simps(y, x)

print(area_np)
print(area_sp)
print(area)


# 11.14(T) 
# 근 구하기(Root Finding methods)
# 이분법, 가위치법, newton법, secant법,....

# 1. 구간법 ( Braketing methods ) : 근이 있을 가능성이 있는 구간을 정해놓고 구간 내에서 근을 찾는 방식
# 2. 반복법 ( Iterative methods ) : 초기값을 주고 반복적인 과정을 통해 근을 구하는 방식


## 1.1 이분법 ( Bisection method )
## 구간 [a, b] 설정
## 근을 구하는 쉬운 방법은 구간 점에서의 방정식 부호를 비교

# 11.15(W)

def f(x):
     return x*np.exp(-x) + 1.0

N = 8
xold = 0.0
xmid = 0.3

for k in range(N):
    xnew = xmid - f(xmid) * (xmid - xold)/(f(xmid) - f(xold))
    xold = xmid
    xmid = xnew
    print(f"{k+1}, x = {xnew:0.4f}")

# 전진차분이나 중간차분식을 넣어서 미분식을 근사식으로 바꿔도 문제는 없음!
# 그러나 시간 복잡도, 알고리즘의 성능을 생각해서 가장 효율적인 방법을 사용하면 됨.


# 12. 행렬 연산

