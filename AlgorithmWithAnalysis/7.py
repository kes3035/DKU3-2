# 공학수치해석 6주차 10월 10일
import numpy as np
## Talyor 급수 식을 기반으로 계산하기

## 데이터 다루기
### 1. 배열에서의 행 연산과 열 연산
### 2. 데이터의 평균과 가중값 평균의 계산
### 3. 데이터의 분산 계산

## 인트로
x = np.array([100, 101, 102])
hap = 0

for i in range(3):
    hap = hap + x[i]
print(f'hap = {hap}')
print('----------------------')
hap = 0
hap = np.sum(x)
print(f'hap = {hap}')
print('----------------------')

## 1. 배열에서의 행 연산과 열 연산
A = np.array([[1, 4, -1], [2, 1, 0], [0, -1, 7]])
hap = 0

for i in range(3):
    # hap = hap + A[i][i] 똑같음
        hap = hap + A[i,i]

print(f'hap = {hap}')
print('----------------------')

## 첫 번째 열의 합을 구하면?
hap = 0
for i in range(3):
    hap = hap + A[1][i]
print(f'hap = {hap}')
print('----------------------')

## 2. 데이터 요소의 평균과 가중값 평균의 계산

x = np.array([100, 102, 104])
n = len(x)
hap = 0
for i in range(n):
     hap += x[i]
xbar = hap/n
print(f'xbar = {xbar}')
print('----------------------')

xbar = np.average(x)
print(f'xbar = {xbar}')
print('----------------------')

## 3. 데이터의 분산 계산

xbar = np.average(x)
dif = abs(x - xbar)**2  #xbar는 상수, x는 벡터? xbar의 벡터화 (파이썬 장점)
var = np.sum(dif)/n

print(f'var = {var}')
print('----------------------')
# var = np.var(x)

