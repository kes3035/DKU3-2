# 10.31 (T)
# 보간법(interpolation)
## 선형 보간법
## 다항식 보간법
## Lagrange 보간법

## 선형 보간법

def lininterp(x):
    equ = f0 + (f1 - f0)/(x1 - x0) * (x - x0)
    return equ

x0 = 2.0
x1 = 3.0
f0 = 1.414
f1 = 1.732

xw = 2.3

intp = lininterp(xw)

print(f'f(x) = {intp:0.3f}')


