#   9월 19일 3주차 파이썬 문법 속성

## 반복문 만들기

x = [4, 3, 2, 1, 0]

for k in range(5):
    print(0.1*x[k]);

## 조건문 만들기

a = 4 # 할당연산자

if a%2 == 0:    # 비교연산자
    print('A');
else:
    print('B');

# 라이브러리(library)

## 파이썬 언어의 큰장점 중 하나는 다양한 라이브러리의 존재
## 대부분 개개인의 자발적 기여에서 비롯된 것, 사용자 급증에 따라 업데이트도 빈번한 편
## 고급 라이브러리를 대부분 무료로 사용할 수 있다는 점이 매력적
## 수치해석과 같은 다양한 수학적 개념을 다루기 위해 이러한 라이브러리의 사용이 필수적

### 1. 별명 붙여서 쓰기
# import numpy as np

# print(np.cos(1.0))

# print(np.exp(3))

### 2. 전체 내용을 불러오는 방법 -> 별로추천하지 않음
# from numpy import*

# print(cos(1.0))


### 3. 필요한 내용만을 불러오는 방법
# from numpy import cos

# print(cos(1.0))
# print(sin(1.0)) 이건 안됨



# 행렬만들기

## 수치해석에서 행렬을 다루는 문제는 매우 중요
## 다양한 알고리즘에서 행렬의 연산 및 변환이 사용되므로, 프로그래밍적으로 구현하기 위해
## 배열(array)로 만들어 다루는 것이 필수적
## 수학분야에서는 행렬이라고 하지만 프로그래밍에서는 배열이라는 용어를 씀

## 행렬을 만들기 위해 numpy에서는 array함수를 사용
import numpy as np

x = np.array([1,2,3])
print(f'x = {x}')

print(x[0])

a = np.array([[1, 2, 1], [3, 1, 1],[4, 1, 2]])
print(a)
print(a[0])   # 행만 뽑아내는 코드
print(a[0,0]) # 값을 뽑아내는 코드
print(a[:,0]) # 열만 뽑아내는 코드

print('')
print('')
print('')
print('')


## 리스트와 배열의 차이점

### 리스트끼리의 덧셈?
### a = [1, 2, 3]
### b = [1, 2, 3]
### c = a + b
### c에는 [1, 2, 3, 1, 2, 3] 이 담김

### 배열끼리의 덧셈?
### a = [1, 2, 3]
### b = [1, 2, 3]
### c = a + b
### c에는 [2, 4, 6] 이 담김


# Jupyter Notebook?

## MarkDown 언어 지원
## LaTeX과 수식
## Jupyter notebook과 보고서 작성
## 수식표기?
### $\intf(x)dx = 3$ => 적분
### $3\times4=12$
### $\sqrt{2}$
### $\frac{1}{x}$

