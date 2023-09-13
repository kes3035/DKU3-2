#   9월 6일 1주차 알고리즘으로 배우는 수치해석

#   수치해석과 시류
##   최근 인공지능이 큰 관심을 끌고 있음. 왜냐면 자율주행 or 로봇과 같은 새로운 분야에서 발전이 있었기 때문.
##   인공지능의 새로운 분야가 궁극적으로 "수치해석" 에 기반을 둠을 알아두자.

##   전통적 수치해석 -> 고전적 수학이론에 기반.
##   문제 해결을 위해 수치해석에서는 여러 "근사적 방법"을 동원했고 이 배경이 정제된 수학이론에서 시작.
##   선형대수, 급수, 미적분, 벡터, 함수론,,,등 고등 수학지식 요구.

###  근사해법? (Approximation) 정답과 가까우리라 생각되는 해답 ( = 근사해)
###  근사해법은 정답이 아님! 그럼 왜? 정답을 모르니까! 정답을 아는 해는 수치해석으로 풀지 않음.

##   수치해석에서 제시하는 문제를 풀기위한 방법은 알고리즘으로 제시.
##   알고리즘은 효율성 극대화를 위해 축약된 상태로 제공, 입문자들이 그 내용을 파악하기 곤란.

##   알고리즘 원리를 이해했더라도, 현실화를 위해 컴퓨터 언어를 사용해서 프로그래밍을 통해 효율성과 정확성 확인.
##   수치해석 입문자가 모든 수준을 갖추기엔 쉽지 않기에 수치해석 분야에 대한 장벽이 높아보이기도 함.

#   수치해석적 방법론
##   수학적 이론이 필수이기에 기본적 내용은 학습 -> 어려운 개념을 효과적으로 제시하기 위함.
##   알고리즘 == 암호문. 풀면 쉽게 이해할 수 있지만, 해독이 되지 않으면 어렵다.
##   프로그래밍으로 검증하기 위해 프로그램 언어에 익숙해질 필요 있음.

### google Colab => Jupyter notebook 무료 제공
### Anaconda


#-------------------------------------------------------
#-------------------------------------------------------


#   9월 12일 2주차 알고리즘으로 배우는 수치해석_수치해석이란?

##   수치해석이라함은 컴퓨터에서 문제를 해결하는 방법에 관한 것이라고 생각하는 경우가 다수
##   문제를 근사적 방법으로 해결하고자 하는 하나의 방법론 ( Approximation <-> True solution )

##   고전적 수치해석(classical numerical analysis) 방법론
##   시류를 반영한 수치해석(contemporary numerical analysis) 방법론
###   - 시대에 뒤떨어지거나 잘못된 것이 아님. 하나의 방법론일 뿐. 강력한 수학적 배경이 필요
###   - 근사해법의 정확성 검증을 위해 오차에 대한 추정 문제(error estimation)를 다뤄야함
###   - 이를 위해 최소한의 미적문(calculus), 벡터이론(vector theory)및 고급 함수론에 대한 지식 필요

#   고전적 수치해석 방법론

##   수학이론 -> 알고리즘 -> 의사코드(pseudo code)
##   수학이론을 가장 중요시 여김. 문제에 대한 근사해법이 결정되면 알고리즘으로 제작.
##   의사 코드는 실제 작동하는 프로그램이 아닌 알고리즘을 프로그램 형태로 설명해 놓은 것

#   시류를 반영한 수치해석 방법론

##   수학이론 -> 알고리즘 -> 프로그램
##   보다 현실적 고민을 해결하고자 하는 노력
##   ex)인공지능, 머신러닝... 수치해석분야에서도 이에 부응하기 위한 변화의 바람이 분다.

##   ⭐️1. 방대한 양의 데이터를 어떻게 다룰 것인가?⭐️
##   ⭐️2. 인공지능 및 머신러닝 관련 프로그램이나 라이브러리를 어떻게 적용할 것인가?⭐️

##   첫 번째 문제는 방대하게 나오는 데이터를 처리하는 문제. 각종 센서와 측정기기가 데이터가 실시간으로 생성중
##   인터넷 사용이 증가->여러 분야에서의 데이터 폭증. (이러한 양적 팽창은 과거에 크게 고려되지 않았음)
##   많은 데이터들 속 필요한 데이터를 찾아 분석하여 결론도출을 위해 데이터를 잘 다룰 수 있는 체계적 방법 필요
##   데이터 과학의 영역에 속함. 통계적 수치 값과 보간법(interpolation), 회귀법(regression)등이 필요
##   다양한 분야에서 제공하는 컴퓨터 라이브러리를 접목
##   파이썬에서는 Numpy, Scipy 등 의 라이브러리 제공
###   import numpy as np


#   두 방법의 차이?
##   과학기술, 통계, 인공지능 라이브러리 --> 알고리즘



#   ⭐️파이썬 언어⭐️

## 데이터타입
### 1. 수

x = 1.1
y = 9
name = 'John' ## or '''John''' or """John"""

print(x)
print(y)
print(name)
### 2. 리스트

list = [] ## initialize
list = ['A', 23, "Bob"]

my_first_list = list[0]
print(my_first_list)

#-------------------------------------------------------
#-------------------------------------------------------


#   9월 13일 2주차 파이썬 문법 속성

## pythonic? => 파이썬스러운
## 변수 네이밍 작업 => 소문자, 대문자(group, GROUP)


## 1. CamelCase
myFirstVariable = "My first variable with Camel Case"
MyFirstVariable = "My first variable with Camel Case"


## 2. SnakeCase
my_first_variable = "My_first_variable_with_Snake_Case"

## 상수같은 경우에는 대문자로 쓰면 좋음 ex) G = 9.81, PLANK = 3.1 or PLANK_NUMBER = 3.1

name = "Elyot"
ID = "32190956"
SCORE = "4.5"
age = 23

x = 3
y = 7
if x>2:
    print(x, y)

##연산자
## +, -, *, /
## in, notin

text = "python is fun"
if "fun" in text:
    print("Exist");

print("")
print("")
print("")
print(text[0])
print(text[4])
print(text[7])
print("")
print("")
print("")
print(len(text))



## slice? [시작:끝]

slicedText = text[9:]
print(slicedText)

## nagative index

nag = text[-1]
print(nag)


# 출력
#  1. %
#  2. format
#  4. f-string


ex1 = 1
ex2 = 3.0
ex3 = ex1/ex2

print(ex3)

print(f'x = {x}')

# if문, for문

## 반복문 만들기

# for i in range(len(text)):
#     print(i);

for i in range(1,6):
    print(i);

## 조건문 만들기

if ex2 > 4:
    print(f'ex2는 4보다 큽니다');
else:
    print(f'ex2는 {ex2}');