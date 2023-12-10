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

def cos(x):
    return np.cos(x)

def trapezoid(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2*f(a + i*h)
    return print(f'사다리꼴 적분공식 = {h*s/2:0.4f}')

def trapezoid_with_data(a, b):
    n = len(b)
    h = (a[n-1]-a[0])/(n-1)
    s = 0.0
    for i in range(n-1):
        s += b[i] + b[i+1]
    return print(f'사다리꼴 적분공식 (데이터) = {h*s/2:0.4f}')


def simpsons_1_3_rule(a, b, n, f):
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    s = f(x[0]) + f(x[n])
    for i in range(1, n):
        if i%2 == 0:
            s += 2*f(x[i])
        else:
            s += 4*f(x[i])
    return print(f'심슨 1/3 적분공식 = {h / 3 * s:0.4f}')

def simpsons_3_8_rule(a, b, n, f):
    h = (b-a)/n
    s = f(a) + f(b)
    for i in range(1, n):
        if i % 3 == 0:
            s += 2*f(a + i*h)
        else:
            s += 3*f(a + i*h)
    return print(f'심슨 3/8 적분공식 = {3 * h / 8 * s:0.4f}')

def gaussian_quad_two(f):
    N = 2
    xi = np.array([1.0/np.sqrt(3), -1.0/np.sqrt(3)])
    w = np.array([1.0, 1.0])
    sums = 0.0
    for i in range(N):
        sums += w[i]*f(xi[i])
    return print(f'2점 Gauss 적분 = {sums:0.4f}')

def gaussian_quad_three(f):
    N = 3
    xi = np.array([0.0, np.sqrt(3.0/5.0), -np.sqrt(3.0/5.0)])
    w = np.array([8.0/9.0, 5.0/9.0, 5.0/9.0])
    sums = 0.0
    for i in range(N):
        sums += w[i]*f(xi[i])
    return print(f'3점 Gauss 적분 = {sums:0.4f}')

def gaussian_quad_two_with_unoptimized_interval(a, b, f):
    x1 = (a + b) / 2 - (b - a) / (2 * (3 ** 0.5))
    x2 = (a + b) / 2 + (b - a) / (2 * (3 ** 0.5))
    integral = ((b - a) / 2) * (f(x1) + f(x2))
    return print(f'구간이 다른 2점 Gauss 적분 = {integral:0.4f}')

def gaussian_quad_three_with_unoptimized_interval(a, b, f):
    # Gaussian Quadrature for 3 points on [-1, 1]
    x1 = -((3/5) ** 0.5)
    x2 = 0
    x3 = (3/5) ** 0.5

    integral = ((b - a) / 2) * (5/9 * f(((b - a) * x1 + a + b) / 2) + 8/9 * f(((b - a) * x2 + a + b) / 2) +
                                5/9 * f(((b - a) * x3 + a + b) / 2))
    return print(f'구간이 다른 3점 Gauss 적분 = {integral:0.4f}')





# 함수랑 구간 주어지고 사다리꼴 적분법으로 답 구하는 문제 trapezoid(적분시작, 적분끝, n, 함수)
#trapezoid(2, 4, 3, f)   

# 데이터를 사다리꼴 적분법으로 답 구하는 문제 (x배열, y배열)
#trapezoid_with_data(np.array([0.0, 1.0, 2.0, 3.0, 4.0]), np.array([1.0, 1.5, 2.0, 2.5, 3.0]))

# 함수랑 구간 주어지고 심슨 적분법으로 답 구하는 문제 (적분시작, 적분끝, n, 함수)
#simpsons_1_3_rule(2, 4, 4, f)

#simpsons_3_8_rule(2, 4, 4, f)

# 함수 주어지고 2점 가우스 적분법 (구간은 -1, 1)
#gaussian_quad_two(cos)

# 함수 주어지고 3점 가우스 적분법 (구간은 -1, 1)
#gaussian_quad_three(cos)

# 함수f가 주어지고 구간이 a,b일 때, 2점 가우스 적분법으로 답 구하는 문제
#gaussian_quad_two_with_unoptimized_interval(2, 4, f)

# 함수f가 주어지고 구간이 a,b일 때, 3점 가우스 적분법으로 답 구하는 문제
#gaussian_quad_three_with_unoptimized_interval(2, 4, f)

#area, error = integrate.quad(f, 2, 4)
#print(f'싸이파이 가우스 적분법 = {area:0.4f}, 오차는 {error:0.4f}')
"""
Simpson 적분공식 -> 사다리꼴 적분공식의 단점을 보완하기 위해 선형 보간법의 차수를 높인 것!
심슨의 1/3 공식
처음과 끝을 제외한 중간들의 x_i값들이 홀수일땐 앞에 4를, 짝수일땐 앞에 2를 곱한다
평균? -> 똑같은 가중치를 주고 계산하는 것

Gauss 구적법 ( Gaussian Quadrature )
특정 위치에서의 함수 값과 그에 해당하는 가중 값의 곱을 합산하여 근사적으로 적분을 계산하는 방법
node : 절점, weight : 가중값
절점과 가중값을 알아야 사용가능
적분구간은 항상 -1부터 +1 까지

르장드르
n개의 구적법을 쓰겠다 == 다항식의 (2n-1)차 까지를 적분하면 실제값과 같다.

데이터를 사용한 적분
실험 데이터등을 사용하여 적분을 구해야하는 경우
예를 들어 자동차의 속도에 대해 적분을 하면 주행거리를 알 수 있다.
또, 미사일의 가속도를 통해 미사일의 속도를 알 수 있다.

"""