# 导入 需要的 library 库  
import numpy as np # 科学计算
import matplotlib.pyplot as plt # 画图
import scipy.signal as sg # 导入 scipy 的 signal 库 命名为 sg

import warnings
warnings.filterwarnings("ignore") # 去掉常规警告

# 方案一，由频率响应函数求解DTFT
def DTFT(xn, n0=0, a=-2*np.pi, b=2*np.pi): # DTFT
    # xn:信号值序列，这里作为分子系数
    # n0:用于计算DTFT的信号xn起始点n=0的位置，也即n<0的信号序列个数
    num =np.array(xn)
    den = np.array([1])
    ws, Hw = sg.freqz(num, a=den, whole=True, worN=np.linspace(a, b, 512)) # 想想为什么DTFT可以这么求解？
    return ws, Hw/np.exp(-1j*ws*n0) # TODO：想想为什么求解出的频率响应要除以一个因子？
    
un = lambda n: np.heaviside(n, 1) # 定义离散阶跃函数u[n]
N = 16 # 离散点数
n = np.arange(-N, N+1)
x1 = un(n+1) - un(n-2)
x2 = un(n+2) - un(n-3)
a = 2
b = -3
x = a*x1 + b*x2
n0 = len(n[n<0]) # 获取n<0的信号序列点数，也是信号起始点n=0的位置
w1, Xw1 = DTFT(x1, n0) # 信号x[n]的DTFT

w2, Xw2 = DTFT(x2, n0)

w, Xw = DTFT(x, n0)

fig, axs = plt.subplots(2, 1, figsize=(10, 10)) # 通过figsize调整图大小
plt.subplots_adjust(wspace = 0, hspace = 0.4) # 通过hspace调整子图间距
plt.subplot(211) # 绘制a*x1[n]+b*x2[n]信号与x[n]信号
_ = plt.stem(n, a*x1+b*x2, use_line_collection=True, linefmt='k', label='a*x1[n]+b*x2[n]')
_ = plt.stem(n, x, use_line_collection=True, linefmt='b', label='x[n]')
_ = plt.legend()
plt.xlabel('n')
plt.grid()

plt.subplot(212) # 绘制a*X1(e^jw)+b*X2(e^jw)信号与X(e^jw)信号
_ = plt.plot(w1, a*Xw1+b*Xw2, w, Xw)
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
_ = plt.legend(['$a*X_1(e^{jw})+b*X_2(e^{jw})$', '$X(e^{jw})$'])
plt.xlabel('omega')
plt.grid()

plt.show()