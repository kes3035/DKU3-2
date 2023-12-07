#32190956 김은상 
#지반가진 시스템의 진동 측정 및 시스템 이해

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

#추 번호에 따른 무게 (g * 0.001 = kg)
weight_1 = 92.6*0.001;
weight_2 = 97.1*0.001;
weight_3 = 96.8*0.001;
weight_4 = 97.1*0.001;
weight_5 = 97.3*0.001;
weight_6 = 97.1*0.001;
weight_7 = 97.1*0.001;

#센서무게 (g * 0.001 = kg)
sensor_23 = 73.6*0.001;
sensor_24 = 73.0*0.001;
sensor_25 = 72.5*0.001;

#캐리지 무게
carrage_1 = 282.9*0.001;
carrage_2 = 283.1*0.001;

#스프링 무게
spring = 2.6*0.001;

#실험에 사용된 무게 ( 볼트무게 무시 )
m1 = weight_2 + weight_3 + weight_4 + weight_5 + 2*spring + carrage_1 + sensor_23;
m2 = weight_4 + weight_5 + 2*spring + carrage_1 + sensor_23;

#질량 1에 대한 w 값 ( 1rpm = pi/60 rad/s )
w_1_1 = 180*np.pi/30;
w_1_2 = 210*np.pi/30;
w_1_3 = 240*np.pi/30;
w_1_4 = 260*np.pi/30;
w_1_5 = 310*np.pi/30;

#질량 2에 대한 w값
w_2_1 = 180*np.pi/30;
w_2_2 = 220*np.pi/30;
w_2_3 = 265*np.pi/30;
w_2_4 = 320*np.pi/30;
w_2_5 = 360*np.pi/30;

#지반가진 진폭
Y = 4;

#영상을 통해 확인한 진폭
X_1_1 = 3;
X_1_2 = 5;
X_1_3 = 25;
X_1_4 = 11;
X_1_5 = 2.5;

X_2_1 = 2.7;
X_2_2 = 3.5;
X_2_3 = 11;
X_2_4 = 6.2;
X_2_5 = 3;

#변위의 전달률
x_over_y_1_1 = X_1_1/Y;
x_over_y_1_2 = X_1_2/Y;
x_over_y_1_3 = X_1_3/Y;
x_over_y_1_4 = X_1_4/Y;
x_over_y_1_5 = X_1_5/Y;

x_over_y_2_1 = X_2_1/Y;
x_over_y_2_2 = X_2_2/Y;
x_over_y_2_3 = X_2_3/Y;
x_over_y_2_4 = X_2_4/Y;
x_over_y_2_5 = X_2_5/Y;


w_n_1 = w_1_3;
w_n_2 = w_2_3;
# r = 0:0.0001:2;
r_cal_1 = w_2_1/w_n_2;
r_cal_2 = w_2_2/w_n_2;
r_cal_3 = w_2_3/w_n_2;
r_cal_4 = w_2_4/w_n_2;
r_cal_5 = w_2_5/w_n_2;

y = [x_over_y_2_1, x_over_y_2_2, x_over_y_2_3, x_over_y_2_4, x_over_y_2_5]
x = [r_cal_1, r_cal_2, r_cal_3, r_cal_4, r_cal_5]

# 주어진 시스템의 파라미터 설정
w_n = 260  # 자연진동주파수 (rad/s)
zeta = 0.1  # 감쇠비
zeta1 = 0.25
zeta2 = 0.3
# 주파수 범위 설정 (r 값에 해당하는 w/w_n 범위)
w = np.linspace(0, 2 * w_n, 1000)
r = w / w_n

# 전달함수 모델 정의
H = 1 / np.sqrt((1 - r**2)**2 + (2 * zeta * r)**2)

H1 = 1 / np.sqrt((1 - r**2)**2 + (2 * zeta1 * r)**2)

H2 = 1 / np.sqrt((1 - r**2)**2 + (2 * zeta2 * r)**2)



# 그래프 그리기
plt.plot(r, H, label="zeta = 0.1")
plt.plot(r, H1, label="zeta = 0.25")
plt.plot(r, H2, label="zeta = 0.3")
plt.grid()
# plt.plot(x, y, "o-", label = "experiment")
plt.title("displacement transmissibility about r")
plt.xlabel("r (w/w_n)")
plt.ylabel("X/Y (displacement transmissibility)")
plt.scatter(np.sqrt(2), 1, c='red', marker='o', label="r=√2")
plt.axvline(x=1, color='gray', linestyle='--', label="r=1")
plt.legend()
plt.show()

