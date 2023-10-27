# 8.7 연습문제
#1, 3, 5, 7

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    output = np.sqrt(x)
    return output
exact_value = 1/(2 * np.sqrt(3.0))

def f3(x):
    output = np.exp(x)*np.cos(x)
    return output
exact_value3 = np.exp(1.0)*(np.cos(1.0)-np.sin(1.0))

def f5(x):
    output = x*np.cos(2*x)
    return output
exact_value5 = np.cos(2.0)-(2.0)*np.sin(2.0)

def f7(x):
    if x==1:
        return 5.1
    elif x==2:
        return 7.5
    elif x==3:
        return 9.1
    elif x==4:
        return 9.3
    else:
        raise ValueError("Plz put the right Data")

# t = np.linspace(0, 3, 1000)
# graph = plt.plot(t, f5(t))

# plt.title("5. Graph")
# plt.xlabel("x")
# plt.ylabel("f(x)")

# plt.show()


def numerical_differentiation(f, x, method='central'):
    h = 1.0
    if method == 'central':
        result = (f(x + h) - f(x - h)) / (2 * h)
        print(f"중간차분식 = {result:0.4f}")
    elif method == 'forward':
        result = (f(x + h) - f(x)) / h
        print(f"전진차분식 = {result:0.4f}")
    elif method == 'backward':
        result = (f(x) - f(x - h)) / h
        print(f"후진차분식 = {result:0.4f}")
    else:
        raise ValueError("Method must be either 'central', 'forward', or 'backward'")
    return result

print("1번문제 -----------------------------------------------------------------")
print(f"실제값    = {exact_value:0.4f}")
num_value_for = numerical_differentiation(f, 3.0, method="forward")
print(f'전진차분에 대한 에러값 = {abs((exact_value-num_value_for)/exact_value)*100:0.1f}%')
num_value_back = numerical_differentiation(f, 3.0, method="backward")
print(f'후진차분에 대한 에러값 = {abs((exact_value-num_value_back)/exact_value)*100:0.1f}%')
num_value_cent = numerical_differentiation(f, 3.0)
print(f'중간차분에 대한 에러값 = {abs((exact_value-num_value_cent)/exact_value)*100:0.1f}%')
print("-----------------------------------------------------------------------")

print("3번문제 -----------------------------------------------------------------")
print(f"실제값    = {exact_value3:0.4f}")
num_value3_for = numerical_differentiation(f3, 1.0, method="forward")
print(f'전진차분에 대한 에러값 = {abs((exact_value3-num_value3_for)/exact_value3)*100:0.1f}%')
num_value3_back = numerical_differentiation(f3, 1.0, method="backward")
print(f'후진차분에 대한 에러값 = {abs((exact_value3-num_value3_back)/exact_value3)*100:0.1f}%')
num_value3_cent = numerical_differentiation(f3, 1.0)
print(f'중간차분에 대한 에러값 = {abs((exact_value3-num_value3_cent)/exact_value3)*100:0.1f}%')
print("-----------------------------------------------------------------------")

print("5번문제 -----------------------------------------------------------------")
print(f"실제값    = {exact_value5:0.4f}")
num_value5_for = numerical_differentiation(f5, 1.0, method="forward")
print(f'전진차분에 대한 에러값 = {abs((exact_value5-num_value5_for)/exact_value5)*100:0.1f}%')
num_value5_back = numerical_differentiation(f5, 1.0, method="backward")
print(f'후진차분에 대한 에러값 = {abs((exact_value5-num_value5_back)/exact_value5)*100:0.1f}%')
num_value5_cent = numerical_differentiation(f5, 1.0)
print(f'중간차분에 대한 에러값 = {abs((exact_value5-num_value5_cent)/exact_value5)*100:0.1f}%')
print("-----------------------------------------------------------------------")

print("7번문제 -----------------------------------------------------------------")
num_value7_for = numerical_differentiation(f7, 2.0, method="forward")
num_value7_back = numerical_differentiation(f7, 2.0, method="backward")
num_value7_cent = numerical_differentiation(f7, 2.0)
print("-----------------------------------------------------------------------")