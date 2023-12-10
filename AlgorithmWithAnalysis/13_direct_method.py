import numpy as np
import scipy.linalg

# 11.28(T)
"""
선형 방정식을 푸는 방법(직접법)
1. 역행렬에 의한 해법 ( 비효율적 - 계산량이 많고 cs적으로 시간복잡도가 높음)
2. LU분해법 ( 실용적 )
3. 콜레스키 분해법 ( 실용적 )
4. 가우스 소거법

대각우세(Diagonally Dominant Matrix)
=> 행렬의 대각선에 있는 값의 절댓값이 나머지 값의 절대값의 합보다 크면 대각 우세

피봇팅(Pivoting)
=> 행렬이 대각우세를 만족하도록 행의 순서를 바꿔주는 작업
"""

# LU 분해법 = 아랫삼각행렬과 윗삼각행렬로 분리하여 계산
def luComposition(A, b):
    P, L, U = scipy.linalg.lu(A)
    invL = np.linalg.inv(L)
    invU = np.linalg.inv(U)

    x = invU @ (invL @ b)
    return print(f'LU분해법 = {x}')

# Cholesky 분해법 = LU분해법과 비슷하지만 계산 효율이 더 좋음, 아랫삼각행렬만 사용
def cholesky(A, b):
    L = scipy.linalg.cholesky(A, lower=True)
    LT = L.T
    invLT = np.linalg.inv(LT)
    invL = np.linalg.inv(L)
    x = invLT @ (invL @ b)
    return print(f'콜레스키 분해법 = {x}')

# Gauss 소거법
## 가장 기본적인 방법
## 효율성은 좋은 편이 아니지만 학습할 가치는 존재


## 오메가는 SOR에서 new 와 old 의 차이값. 따라서 오메가가 크면 두 차이값을 많이 반영하겠다는 의미
A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])

luComposition(A, b)
cholesky(A, b)

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

