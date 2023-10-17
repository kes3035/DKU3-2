import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(0, 4*np.pi, 1000)
Y = np.sin(X)
Z = -10*np.sin(3*X)
R = 30*np.cos(X)
B = Z+R

ax = plt.subplot()
bx = plt.subplot()
ax.plot(X, B, "C8", markevery = 10)

plt.title("-10sin(3x) + 30cos(x)")
plt.xlabel("x [sec]")
plt.ylabel("Amplitude")
plt.legend("graph1")
plt.annotate("P", (X[200], B[200]), ha = "center", va = "center", arrowprops = {"arrowstyle" : "->", "color" : "C4"})
plt.grid(True)


plt.show()


a = np.array([[50, 6],[90, 7], [30, 5], [10, 2]])
a13 = np.sum(a[0,:])
a23 = np.sum(a[1,:])
a33 = np.sum(a[2,:])
a43 = np.sum(a[3,:])

print(f'7.6.1) a13, a23, a33, a34 = {a13}, {a23}, {a33}, {a43}')

a = np.array([[59, 6], [98, 7], [37, 5], [16, 2]])
b1 = np.sum(a[:,0])
b2 = np.sum(a[:,1])
c1 = np.average(a[:,0])
c2 = np.average(a[:,1])

print(f'7.6.3) b1, b2 = {b1}, {b2} c1, c2 = {c1}, {c2}')

a = np.array([[5, 26], [9, 27], [3, 25], [1, 22]])
b1 = np.sum(a[:,0])
b2 = np.sum(a[:,1])
c1 = np.average(a[:,0])
c2 = np.average(a[:,1])

print(f'7.6.5) b1, b2 = {b1}, {b2} c1, c2 = {c1}, {c2}')

a = np.array([[35, 6], [39, 7], [33, 5], [31, 2]])
a13 = np.sum(a[0,:])
a23 = np.sum(a[1,:])
a33 = np.sum(a[2,:])
a43 = np.sum(a[3,:])
b1 = np.sum(a[:,0])
b2 = np.sum(a[:,1])
c1 = np.average(a[:,0])
c2 = np.average(a[:,1])
print(f'7.6.7) a13, a23, a33, a34 = {a13}, {a23}, {a33}, {a43}')
print(f'       b1, b2 = {b1}, {b2} c1, c2 = {c1}, {c2}')

a = np.array([[5, 96], [9, 97], [3, 95], [1, 92]])
a13 = np.sum(a[0,:])
a23 = np.sum(a[1,:])
a33 = np.sum(a[2,:])
a43 = np.sum(a[3,:])
b1 = np.sum(a[:,0])
b2 = np.sum(a[:,1])
c1 = np.average(a[:,0])
c2 = np.average(a[:,1])
print(f'7.6.9) a13, a23, a33, a34 = {a13}, {a23}, {a33}, {a43}')
print(f'       b1, b2 = {b1}, {b2} c1, c2 = {c1}, {c2}')


