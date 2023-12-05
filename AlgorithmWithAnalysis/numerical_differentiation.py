# 기말 범위 시작
import numpy as np
"""
미분식 (Differential)
차분식 (Difference)
 1. 전진차분(Forward)
 2. 후진차분(Backward)
 3. 중간차분(Centered)
"""

# 정의된 함수
def f(x):
    return x*np.exp(-x)

def forwardDiff(func, xi, h):
    xpi = xi + h
    return print((func(xpi) - func(xi))/h)

def backwardDiff(func, xi, h):
    xmi = xi - h
    return print((func(xi) - func(xmi))/h)

def centeredDiff(func, xi, h):
    xpi = xi + h
    xmi = xi - h
    return print((func(xpi) - func(xmi))/(2*h))

# 문제풀이 방법
# 함수를 작성하고, 원하는 차분식 불러와 실행
# ex) f(x) = xe^(-x)인 경우

centeredDiff(f, 2, 0.1) # 각각 순서대로 사용할 함수, 위치, 간격

"""
수치미분의 유용성
1. 해석적으로 미분이 불가능한 대상, 복잡한 함수나 데이터에 대하여 차분식을 통해 근사적 미분 수행 가능
2. 인공신경망 등에서 데이터를 적합하기 위해 목적함수의 최적값을 구해야하는데, 이때 복잡한 함수와 대용량의 데이터에 대해 수치미분 활용 필수적
3. 일반적으로 수치미분의 활용 사례가 잘 보이지 않을 수 있으나, 물리적 법칙이 적용되는 분야에서 수치미분의 적용이 필연적
"""

