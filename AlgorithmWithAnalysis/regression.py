# 11.29 (W)
# 회귀법 : 종속변수와 독립변수와의 관계를 알아보기 위함
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

e    = e1 ^2 + e2 ^2 + .... + en ^2
     = sum(y- y_hat)^2

결국 오차는 베타의 함수  => 오차를 최소화 하는 베타 존재
                   => 오차를 beta_0, beta_1에 대해 각각 편미분한 값이 0
                   => 제곱을 더한 것에 루트를 씌우지 않은 이유 ( 해도 결국 똑같음 )

다항식 보간법이 선형보다 무조건 좋은 것이 아님! 
선형 -> 직관적
다항식-> 디테일
"""

# 회귀법의 정확도
## SSR(the Sum of Squares Residuals), SST(the Sum of Squares Total)
## 오차를 제곱한 항을 합한 것, 전체 제곱을 합한 것의 "비"
## R^2 = 1 - (SSR)/(SST)           (SSR = epsilon)
## R^2 -> 1에 수렴하도록 하는 것이 이상적 
## SST = sigma (y_i - y_bar)^2

# 비선형 회귀법
# log(y_hat) = log(a) + bx
