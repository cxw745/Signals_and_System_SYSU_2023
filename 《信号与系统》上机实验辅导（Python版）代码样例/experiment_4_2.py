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

# 方案二，由课本公式(5.9)求解DTFT
# def DTFT(n, xn, a=-2*np.pi, b=2*np.pi):
#     # n:离散时间序列
#     # xn:信号值序列，想想方案二离散时间信号x[n]应满足什么条件
#     ws = np.linspace(a, b, 1024) # 频率取点
#     Xw = np.zeros_like(ws, dtype=complex)
#     for i in range(len(ws)):
#         Xw[i] = np.sum(xn*np.exp(-1j*ws[i]*n)) # 利用公式计算DTFT
#     return ws, Xw

n = np.arange(64) # 定义序号
n0 = len(n[n<0]) # 获取n<0的信号序列个数。TODO：想想为什么要获取起始点位置？
print(n0)
a = 0.3 # 指数底数
un = lambda n: np.heaviside(n, 1) # 定义离散阶跃函数u[n]
xn = np.power(a, n)*un(n) # 指数序列
fs = 2*np.pi # 频域范围
w, Xw = DTFT(xn, n0, -fs, fs) # 方案一求解DTFT，频域范围默认[-2π, 2π]
# w, Xw = DTFT(n, xn, -fs, fs) # 方案二求解DTFT，频域范围默认[-2π, 2π]

fig, axs = plt.subplots(2, 1, figsize=(10, 10)) # 通过figsize调整图大小
plt.subplots_adjust(wspace = 0, hspace = 0.4) # 通过hspace调整子图间距
plt.subplot(211) # 绘制x[n]信号的子图
plt.plot(w, np.abs(Xw)) # 绘制随时间衰减的指数信号DTFT幅频图
# plt.plot(w, np.abs(Xw), w, np.abs(1/(1-a*np.exp(-1j*w)))) # 第二个图为解析解形式
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('$\omega$')
plt.title('Amplitude Value:$|X(e^{jw})|$')
plt.grid() # 显示网格

plt.subplot(212) # 绘制x[n]傅里叶变换的子图
plt.plot(w, np.angle(Xw)) # 绘制随时间衰减的单边指数信号DTFT相频图
# plt.plot(w, np.angle(Xw), w, np.angle(1/(1-a*np.exp(-1j*w)))) # 第二个图为解析解形式
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('$\omega$')
plt.title('Phase Value:$\measuredangle X(e^{jw})$') # ∡
plt.grid() # 显示网格
plt.show() # 显示图像