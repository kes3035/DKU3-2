# 파이썬 보강-1

## naming

### 소문자와 대문자
### 소문자 대문자 모두 변수명에 사용될 수 있지만 물리적상수값은 대문자로 쓰는 경향이 있음

### Camel Case, Snake Case

camelCaseVariable = "이것은 카멜케이스 변수 예시입니다."
snake_case_variable = "이것은 스네이크 케이스 변수 예시입니다."

### 변수의 가장 앞글자를 대문자로 쓰는 것은 상관이 없지만,
### 프로그래밍 언어에서 사용되는 구조체 혹은 클래스가 대문자를 사용하는 경향이 있기에
### 일반 변수는 소문자로 시작하는 것을 더 지향.

## 프린트

print(camelCaseVariable)
print(snake_case_variable)
print(type(camelCaseVariable))


print("")
print("")
print("")

## 변수 바인딩

camelCaseVariable = "변수에 새로운 값을 넣었습니다"
print(camelCaseVariable)

x = 3.14
y = 1


print("")
print("")
print("")


## 연산자 ( +, -, *, /, %,...)
### 나눗셈은 분모에 0이 들어가면 안됨! 에러메세지



z = x + y
print(z)
print(type(z))
print(f'z^3 = {z**3}')


print("")
print("")
print("")

## list

myFirstList = [] ## initialize
myFirstList = ["0번째", "1번째", "2번째"]
print(myFirstList[0])

print("")
print("")
print("")


# 파이썬 보강-2

mySecondList = []
mySecondList = ["python", 2.1, "is", "Fun", 4]
print(mySecondList)

print("")
print("")
print("")

print(mySecondList[0] + " " + mySecondList[2] + " " + mySecondList[3])

## 반복문

for element in mySecondList:
    print(element);

print("")
print("")
print("")

for i in range(len(mySecondList)):
    print(i);

print("")
print("")
print("")

## 구구단 출력하기

for i in range(0,10):
    for j in range (0,10):
        print(f"{i} x {j} = {i*j}");

print("")
print("")
print("")

## 조건문 if, else

myTestScore = 89.0

if myTestScore >= 90:
    print("A입니다.");
else:
    print("A가 아닙니다.");

print("")
print("")
print("")