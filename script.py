import codecademylib
from matplotlib import pyplot as plt

x = [1999,2000, 2001, 2002, 2003, 2004]
y1 = [15, 20, 25, 30, 35, 40]
y2 = [4000, 6000, 8000, 10000, 12000, 14000]

plt.plot(x, y1, marker='o', color='pink')
plt.plot(x, y2, marker='o', color='gray')

plt.title("Two Lines on One Graph")
plt.xlabel("Amazing X-axis")
plt.ylabel("Incredible Y-axis")

plt.legend(["Y1","Y2"], loc=5)

plt.show()