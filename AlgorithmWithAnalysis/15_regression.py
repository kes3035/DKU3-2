import numpy as np
import matplotlib.pyplot as plt
"""
선형 회귀법
다항식 회귀법
비선형 회귀법 
-> 최소 자승법(method of leat squares)

ex) 하루 커피 섭취량과 수면 시간의 관계
독립 변수 : 커피 섭취량 (x)
종속 변수 : 수면 시간  (y)

y = y_hat + e
  = beta_0 + beta_1 * x + e
  
beta_0, beta_1 : 정해야할 계수
             e : 오차

행렬로 표기한 베타 = inv(X.T @ X) @ X.T @ y

e    = e1 ^2 + e2 ^2 + .... + en ^2
     = sum(y- y_hat)^2

결국 오차는 베타의 함수  => 오차를 최소화 하는 베타 존재
                   => 오차를 beta_0, beta_1에 대해 각각 편미분한 값이 0
                   => 제곱을 더한 것에 루트를 씌우지 않은 이유 ( 해도 결국 똑같음 )

다항식 보간법이 선형보다 무조건 좋은 것이 아님! 
선형 -> 직관적
다항식-> 디테일

회귀법의 정확도 -> SSR(Sum of Squares Residuals), SST(Sum of Squares Total)
오차를 제곱한 항을 합한 것, 전체 제곱을 합한 것의 "비"
R^2 = 1 - (SSR)/(SST)           (SSR = epsilon)
R^2 -> 1에 수렴하도록 하는 것이 이상적 
SST = sigma (y_i - y_bar)^2

비선형 회귀법
log(y_hat) = log(a) + bx
"""
# 선형 회귀법
def regression(x, y):
  n = len(x)

  beta0_nom = np.sum(y)*np.sum(x**2) - np.sum(x)*np.sum(x*y)
  denom = n*np.sum(x**2) - (np.sum(x))**2 
  beta0 = beta0_nom / denom

  beta1_nom = n*np.sum(x*y) - np.sum(x)*np.sum(y)
  beta1 = beta1_nom / denom
  ybar = np.average(y)

  yhat = beta0 + beta1 * x  
  print(f'선형회귀법 yhat = {yhat}')
  print(f'선형회귀법 beta0 = {beta0}, beta1 = {beta1}')
  print(f'선형회귀법 정확도 R2 = {R2(y, yhat, ybar):0.4f}')

# 다항식 회귀법
def regression_polynomial(x, y):
  xsq = x**2
  X = np.column_stack([np.ones(len(x)), x, xsq])
  XT = X.T
  beta = np.linalg.inv(XT @ X) @ (XT @ y)


  ybar = np.average(y)
  print(f'다항식 회귀법 beta0 = {beta[0]:0.2f}') 
  print(f'다항식 회귀법 beta1 = {beta[1]:0.2f}') 
  print(f'다항식 회귀법 beta2 = {beta[2]:0.2f}')

  y_hat = X @ beta
  print(f'다항식 회귀법 y_hat = {y_hat}') 
  print(f'다항식회귀법 정확도 R2 = {R2(y, y_hat, ybar):0.4f}')


# 회귀법의 정확도
def R2(y, yhat, ybar):
  SSR = np.sum((y-yhat)**2)
  SST = np.sum((y-ybar)**2)
  R2 = 1 - SSR/SST
  return R2


x = np.array([1, 2, 3, 4, 5])
y = np.array([8.5, 7.7, 6.9, 4.5, 2])

regression(x, y)
regression_polynomial(x, y)