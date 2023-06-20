import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# Define the input signal f[k]
def f(k):
    return np.exp(-2*k) * (k >= 0)


y = []
k_list = range(0, 20)
for i in k_list:
    if i == 0:
        y.append(f(i) - f(i-1))

    elif i == 1:
        yi = f(i) - f(i-1) - 0.5*y[i-1]
        y.append(yi)

    else:
        yi = f(i) - f(i-1) - 0.5*y[i-1] - y[i-2]
        y.append(yi)

plt.title("该离散系统零状态响应")
plt.xlabel("k")
plt.ylabel("y[k]")
plt.stem(k_list[1:], y[1:], label="y[k]")
# 设置横坐标间距
plt.xticks(range(0, 20, 1))
# 显示网格线
plt.grid()
# 显示图例并设置位置
plt.legend(loc=1)
# 显示数值
for x, y in zip(k_list[1:], y[1:]):
    plt.text(x+0.1, y, '%.3f' % y, ha='left', va='top', fontsize=11)
plt.show()



