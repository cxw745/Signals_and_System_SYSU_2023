# 导入 需要的 library 库  
import numpy as np # 科学计算
import matplotlib.pyplot as plt # 画图
import scipy.signal as sg # 导入 scipy 的 signal 库 命名为 sg
from scipy.integrate import quad, simps # 用于求积分

import warnings
warnings.filterwarnings("ignore") # 去掉常规警告

w = np.linspace(-2*np.pi, 2*np.pi, 512) # 频域值
a = 0.3 # 原信号底数
# Xw = (1-a**2)/(1-2*a*np.cos(w)+a**2)
Xw = lambda w: (1-a**2)/(1-2*a*np.cos(w)+a**2)
N = 16 # 离散信号x[n]点数
n = np.arange(-N, N+1) # 定义序号
xn = np.zeros_like(n, dtype=float) # 时域信号值，这里一定要显示设置dtype=float，否则默认为int32
for i in range(len(n)): # 用于计算离散信号x[n]
    # xn[i] = quad(lambda w:(1-a**2)/(1-2*a*np.cos(w)+a**2)*np.exp(1j*w*n[i]), 0, 2*np.pi)[0]/(2*np.pi)
    xn[i] = quad(lambda w: Xw(w)*np.exp(1j*w*n[i]), 0, 2*np.pi)[0]/(2*np.pi)
    # xn[i] 的计算也可以采用数值解，如下复合梯形积分或者辛普森积分公式，还可以采用矩形积分等等...
    # xn[i] = np.trapz(Xw * np.exp(1j*w*n[i]), w)/(w[-1] - w[0]) # 复合梯形积分，积分默认区间为[-2π, 2π]，w[0]=-2π，w[-1]=2π
    # xn[i] = simps(Xw * np.exp(1j*w*n[i]), w)/(w[-1] - w[0]) # 辛普森积分，积分默认区间为[-2π, 2π]，w[0]=-2π，w[-1]=2π

fig, axs = plt.subplots(2, 1, figsize=(10, 10)) # 通过figsize调整图大小
plt.subplots_adjust(wspace = 0, hspace = 0.4) # 通过hspace调整子图间距
plt.subplot(211) # 绘制x[n]信号DTFT的幅度子图，因为X(e^jw)是实函数，所以也可以绘制X(e^jw)本身
_ = plt.plot(w, Xw(w))
plt.title('Amplitude Value:$X(e^{jw})$')
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('$\omega$')
plt.grid()

plt.subplot(212) # 绘制x[n]信号本身
_ = plt.stem(n, xn) # 注意，离散信号用stem绘制
plt.title('x[n]')
plt.xlabel('n')
plt.grid()

plt.show()