# 11.21 (W)
## 행렬연산

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])
print(f'c = {a@b}')

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



# 11.28(T)
"""
선형 방정식을 푸는 방법(직접법)
1. 역행렬에 의한 해법 ( 비효율적 - 계산량이 많고 cs적으로 시간복잡도가 높음)
2. 대각우세
3. 싸이파이
4. LU분해법 ( 실용적 )
5. 피봇팅
6. 콜레스키 분해법 ( 실용적 )
7. 가우스 소거법
"""

## 오메가는 SOR에서 new 와 old 의 차이값. 따라서 오메가가 크면 두 차이값을 많이 반영하겠다는 의미
