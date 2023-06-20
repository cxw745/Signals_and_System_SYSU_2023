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
omega_0 = np.pi
rect = un(n+2) - un(n-3) # 矩形信号
n0 = len(n[n<0]) # 获取n<0的信号序列点数，也是信号起始点n=0的位置
w_rect, Xw_rect = DTFT(rect, n0) # 矩形信号DTFT频谱

x = rect*np.cos(omega_0*n) # 矩形信号频移后的信号
w, Xw = DTFT(x, n0) # 矩形信号频移后的频谱

fig, axs = plt.subplots(2, 1, figsize=(10, 10)) # 通过figsize调整图大小
plt.subplots_adjust(wspace = 0, hspace = 0.4) # 通过hspace调整子图间距
plt.rcParams['font.family']=['SimHei'] # 显示中文
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
plt.subplot(211) # 绘制矩形信号的频谱
_ = plt.plot(w_rect, Xw_rect)
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('omega')
plt.title('矩形信号频谱')
plt.grid()

plt.subplot(212) # 绘制矩形信号频移后的频谱
_ = plt.plot(w, Xw)
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('omega')
plt.title('矩形信号频移后的频谱')
plt.grid()

plt.show()