# 보간법(interpolation)
## 선형 보간식
## 사용법: 순서대로 아는x 값 두개 y값 2개 넣고, 원하는 x값 넣기
## ex) 2, 5, 0.2706, 0.0336, 3.3?

def linInterp(x0, x1, y0, y1, at):
    return print(f'선형 보간법 = {y0 + (y1 - y0)/(x1 - x0) * (at - x0):0.4f}')  

def polynomInterp(x0, x1, x2, y0, y1, y2, at):
    beta0 = y0
    beta1 = (y1-y0)/(x1-x0)
    beta2 = ((y2-y1)/(x2-x1) - (y1-y0)/(x1-x0))/(x2-x0)
    return print(f'다항 보간법 = {beta0 + beta1*(at - x0) + beta2*(at - x0)*(at-x1):0.4f}')

def lagrangeLin(x0, x1, y0, y1, at):
    return print(f'라그랑지 선형 = {((at-x1)/(x0-x1))*y0 + ((at-x0)/(x1-x0))*y1:0.4f}')

def lagrangePoly(x0, x1, x2, f0, f1, f2, xw):
    return print(f'라그랑지 다항{(xw - x1)*(xw - x2)/((x0 - x1)*(x0 - x2))*f0 + (xw - x0)*(xw - x2)/((x1 - x0)*(x1 - x2))*f1 + (xw - x0)*(xw - x1)/((x2 - x0)*(x2 - x1))*f2:0.4f}')


linInterp(2, 3, 1.414, 1.732, 2.3)  #선형보간

polynomInterp(2.0, 4.0, 5.0, 0.2706, 0.0732, 0.0336, 3.3)   #다항보간

lagrangeLin(2, 3, 0.2706, 0.1493, 2.3)  #선형라그랑지

lagrangePoly(2, 3, 5, 0.2706, 0.1493, 0.0336, 2.3)  #다항라그랑지

"""
⭐️보간법의 정확도⭐️
보간법의 주 목적이 알지 못하는 지점 또는 실험이나 계측에서 측정되지 않은 지점에서의 값 추정
정확도에 대해서 언급하기 난해
ex) 시간마다 온도 측정, 만약 특정 시간에서의 측정 누락, 그 시간으로 돌아가서 측정 불가
⭐️고차의 보간식이 무조건적으로 더 좋은 것은 아님⭐️
"""