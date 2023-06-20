import numpy as np
import matplotlib.pyplot as plt

# p_n =p_n-1(1+r)-X，借贷等额本息模型
# 单位是（万）
# A是总额 r是利率 n是周期数
A = 500000
print('贷款总额为 %d'%A)

# 计算每个月应还款的钱数
def X(A, r, n):
    return (r*A*(1+r)**n)/((1+r)**n-1)

x = np.arange(60,372,12)
r = np.arange(0.05/12,0.31/12,0.01/12)
y = np.array(X(A,r,x))
total = y*x
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

#plt.plot(x,y,linestyle='--',marker='o')
plt.plot(x,total,linestyle='--',marker='x')
plt.twinx()
plt.xlim(30,400)
plt.ylim(0,5700000)

plt.legend(['周期还贷额X / 元','总还款额sum / 元'],loc = 1)
plt.show()
print('30years total %.3f'%(sum(y)))

xx = X(A, 0.08/12, 15*12)
print('every month should pay %.3f'%xx)
yy = xx*15*12
print('total should pay %.3f'%yy)