import numpy as np
import scipy.linalg
"""
반복법(Iterative Methods)
- 역행렬의 계산에 대한 부담을 줄이기 위한 방법
1. Jacobi = D + L + U
2. Gauss-Seidel = 자코비와 비슷하지만 서로 연관성을 지님
3. SOR(Successive-Over-Relaxion) = 미지수를 갱신하는 과정에서 분량이 상대적 방향과 관련 있다고 생각
                                => 완화계수를 조절하여 방정식의 수렴도를 어느정도 조절 가능 보통 (0<w<1)

"""
# Jacobi 방법
def jacobi(A, b, n, xo):
    xold = xo
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
def gaussSeidel(A, b, n, xo):
    xold = xo
    L = np.tril(A,-1)
    U = np.triu(A,1)
    D = np.diag(np.diag(A))

    former = np.linalg.inv(L + D) 

    for k in range(n):
        latter = b - U @ xold
        xnew = former @ latter
        xold = xnew
    return print(f'가우스 세이델 방법 = {xnew}')

def sor(A, b, n, xo, omega):
    xold = xo
    L = np.tril(A,-1)
    U = np.triu(A,1)
    D = np.diag(np.diag(A))

    former = np.linalg.inv(L + D/omega)

    for k in range(n):
        latter = (D/omega - D - U)@ xold + b
        xnew = former @ latter
        xold = xnew
    print(f'SOR 방법 = {xnew}')

A = np.array([[2,1,0],[1,4,-1],[0,-1,7]])
b = np.array([4,6,19])
xold = np.array([0.0, 0.0, 0.0])

jacobi(A, b, 10, xold)
gaussSeidel(A, b, 10, xold)
sor(A, b, 10, xold, 1.5)



