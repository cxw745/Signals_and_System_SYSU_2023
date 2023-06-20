import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False


# plt.ticklabel_format(style='plain')     # 关闭科学计数法

# 计算X
class repayments:
    def __init__(self, A, r, n):
        self.a = A
        self.r = r
        self.n = n

    def x(self):
        x = self.a * self.r * (1 + self.r) ** self.n
        x /= (1 + self.r) ** self.n - 1
        return x

    def sum(self):
        return self.n * self.x()


A = 500000
r = 0.05 / 12
n = 60

# 还款月数
n_list = range(60, 372, 12)
r_list = range(5, 31, 1)
# 月利率
r_list = np.divide(r_list, 1200)

x_list = []
sum_list = []
for i in range(len(n_list)):
    t = repayments(A, r_list[i], n_list[i])
    sum_list.append(n_list[i] * t.x())
    x_list.append(t.x())

print('问题1',end='')
print('\n-----------------------\n')
for n, x, sum in zip(n_list, x_list, sum_list):
    print('还款周期为\t%d\t 每月还款金额为\t %f\t还款总额为\t%f\t' % (n, x, sum))
print('\n-----------------------\n')

fig = plt.figure()
ax1 = fig.subplots()
ax2 = ax1.twinx()
ax1.plot(n_list, x_list, '--', linewidth=1.5, label='周期还贷额X / 元', marker='o')
ax2.plot(n_list, sum_list, 'g--', linewidth=1.5, label='总还贷额SUM / 元', marker='x')

ax1.set_xlabel('时间n / 月')
ax1.set_ylabel('周期还贷额X / 元')
ax2.set_ylabel('总还贷额SUM / 元')

plt.grid()
ax1.legend(loc=0)
ax2.legend(loc=1)
plt.show()

# fig, ax = plt.subplots(1, 2)
# ax[0].plot(n_list, x_list, 'r-', linewidth=1.5)
# ax[0].plot(n_list, r_list, 'b--', linewidth=1.5)
# ax[0].set_xlabel('时间n / 月')
# ax[0].set_ylabel('周期还贷额X / 元')
# ax01 = ax[0].twinx()
# ax01.set_ylabel('月利率 / %')

# ax[1].plot(n_list, )  # 画子图2的第一个y轴值
# ax[1].set_ylabel('总还贷额SUM / 元')

# plt.grid()
# plt.show()

print('问题2',end='')
print('\n-----------------------\n')
print("贷款额:50万元  年利率:8%   还贷周期:15年")
temp = repayments(A, 0.08 / 12, 12 * 15)
print("每月应该还贷 %.6f 元" % temp.x())
print("总共应付给银行 %.6f 元" % temp.sum())
print('\n-----------------------\n')
