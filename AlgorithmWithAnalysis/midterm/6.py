# 10월 4일 5주차 수치해석과 오차

## 수치해석은 컴퓨터를 사용하기에 계산의 결과는 정확할 것이라 생각할 수 있다.
## 그러나, 오히려 오차에 대한 고려를 더 해주어야 한다.
## 수치해석의 모든 내용은 오차를 포함하고 있음을 숙지.

## 오차의 종류?
#1. "반올림 오차" (round-off errors)
#2. "절단 오차"  (truncation errors)

### 반올림 오차
## 실 값과 근사값의 차이에서 비롯 ex) 3.141592...
## 컴퓨터의 저장 능력이 유한하기 때문에 무한한 자리 수의 숫자를 저장할 수 없다.
import numpy as np
pi = np.pi
pi2 = 3.14
pi6 = 3.141592

print("반올림 오차의 예시------------------------------")
print(f'pi2 * pi2 = {pi2 * pi2}')
print(f'pi2 * pi6 = {pi2 * pi6}')
print(f'pi6 * pi6 = {pi6 * pi6}')
print(f'pi  *  pi = {pi * pi}')
print("--------------------------------------------")

### 절단 오차
## taylor 급수? -> 복잡한 함수를 간단한 함수의 집합으로 변환
## 해당 변환 과정에서 잘라내는 항들이 오류로 축적

# import matplotlib.pyplot as plt

# plt.plot([1, 2, 3, 4])
# plt.show()

x = 1.0

# Taylor Series if exp(x)

tay1 = 1
tay2 = tay1 + x
tay3 = tay2 + x**2/2
tay4 = tay3 + x**3/6
tay5 = tay4 + x**4/24

print(f'1 term(s) : {tay1:0.4f}')
print(f'2 term(s) : {tay2:0.4f}')
print(f'3 term(s) : {tay3:0.4f}')
print(f'4 term(s) : {tay4:0.4f}')
print(f'5 term(s) : {tay5:0.4f}')

# Errors

exact = np.exp(x)   #exp(x)
err1 = (tay1 - exact)/exact * 100
err2 = (tay2 - exact)/exact * 100
err3 = (tay3 - exact)/exact * 100
err4 = (tay4 - exact)/exact * 100
err5 = (tay5 - exact)/exact * 100

print(f'1 term(s) error : {abs(err1):0.1f}%')
print(f'2 term(s) error : {abs(err2):0.1f}%')
print(f'3 term(s) error : {abs(err3):0.1f}%')
print(f'4 term(s) error : {abs(err4):0.1f}%')
print(f'5 term(s) error : {abs(err5):0.1f}%')

x = 1.0

exptay = [1, x, x**2/2, x**3/6, x**4/24]
sums = 0
for i in range(5):
    sums += exptay[i]
    print(f'{i+1} term(s) : {sums:0.4f}')


# 데이터 다루기OT

## 많은 양 데이터를 다루기 위해 수치해석적 지식과 프로그래밍 지식이 어느정도는 필요
## 데이터에서 중요한 정보를 얻어내기 위해 기본적으로 통계적 처리가 필요
# hap = 0
# x = np.array([100, 101, 102])
# for i in range(3):
#     hap += x[i]
# print(f'hap = {hap}')

# 위와 같은 코드를 numpy 내부의 메서드를 통해 간단하게 구현

x = np.array([100, 101, 102])
hap = np.sum(x)             #numpy에서 제공하는 sum 메서드의 속도는 굉장히 빠름

print(f'hap = {hap}')