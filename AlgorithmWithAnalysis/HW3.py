# 5.5 연습문제

## 5.5.1
N = 5
xold = 0.1
for k in range(N):
    xnew = 1.5*xold
    print(f'k = {k+1}, x= {xnew:0.4f}')     #0.4f => 소수점 출력관한것
    xold = xnew;    
print('------------------')
#위의 경우 N이 무한대로 가면 값이 무한대로 가기 때문에 발산하고
xold = 0.1
for k in range(N):
    xnew = 0.5*xold
    print(f'k = {k+1}, x= {xnew:0.4f}')     #0.4f => 소수점 출력관한것
    xold = xnew;    
#위의 경우 N이 무한대로 감에 따라 값이 0이라는 값에 수렴한다.


## 5.5.3
N = 3
x = 1
for k in range(N):
    x = 2.1*x + 1;
print(f'3번문제의 답은{x}')

## 5.5.5
N = 3
x = 1
for k in range(N):
    x = 0.1*x - 1;
print(f'5번문제의 답은{x}')

## 5.5.7
N = 3
x = 1
for k in range(N):
    x = 1.3*x - 1;
print(f'7번문제의 답은{x}')

## 5.5.9
N = 5
x = 1
for k in range(N):
    x = 0.1*x;
print(f'9번문제의 답은{x}')
