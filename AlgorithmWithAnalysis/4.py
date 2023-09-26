#   9월 26일 4주차 알고리즘으로 배우는 수치해석

## 연산이해하기
# 인공지능의 궁극적 목표는 사람이 생각하는 것과 비슷하게 생각하는 하드웨어와 소프트웨어를 만드는 것
# 기술이 발전해도 현재 인간이 문제 해결하는 방법이 최선의 길이 될지도 모름
# 수치해석에서 배우는 다양한 해법은 사람이 보기에 복잡해 보일 순 있으나, 컴퓨터로 가장 효율적으로 
# 해결할 수 있는 방식과 관련


## 1. 정보의 최소 단위와 이진수

## bit -> 0 or 1
## 8bit -> 2^8 = 256가지수
## 기본적으로 컴퓨터에서는 모든 숫자를 이진수로 변환처리하여 사용
## 다량의 연산으로 인해 수치적인 오차가 발생할 수 밖에 없다.


## 2. 컴퓨터 연산에 대한 이해


##4X2 = 4 + 4
##8X3 = 8 + 8 + 8
##6X4 = 6 + 6 + 6 + 6
##11/2 = 11 -2 -2 -2 -2 -2
##15/3 = 15 -3 -3 -3 -3 -3 
##19/4 = 19 -4 -4 -4 -4


## 3. 파이썬 함수 bin()과 int() 사용법
### 덧셈
a = 0b1011    #0b를 붙이면 이진수라는 것을 알려줌
b = 0b0010
print(type(a))
c = int(a) + int(b)
print(bin(c)) # binary -> 이진수로 출력


### 뺄셈
d = int(a) - int(b)
print(bin(d))

### 곱셈
e = int(a) + int(a) + int(a)
print(bin(e))

## 나눗셈
f = int(a) - int(b) - int(b) - int(b)
print(bin(f))

## 4. 비트 단위 연산(bit-wise arithmetic)

## 자리수가 움직였다? == 2를 곱했다
## 3*4 => 12 <- 1100 (2를 곱함)<- 0110 (2를 곱함)<- 0011

## 3 X 4 = 12

a = 3
sleft2 = bin(a<<2)
print(sleft2)
print(int(sleft2,2))

a = 10
sright = bin(a>>1)
print(sright)
print(int(sright,2))