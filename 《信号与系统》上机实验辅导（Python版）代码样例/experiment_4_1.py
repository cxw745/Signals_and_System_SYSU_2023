# 导入 需要的 library 库  
import numpy as np # 科学计算
import matplotlib.pyplot as plt # 画图

import warnings
warnings.filterwarnings("ignore") # 去掉常规警告

w = np.linspace(-2*np.pi, 2*np.pi, 512) # 频域值
N1 = 2
Hw = np.sin((N1+0.5)*w)/np.sin(w/2)
fig, axs = plt.subplots(2, 1, figsize=(10, 10)) # 通过figsize调整图大小
plt.subplots_adjust(wspace = 0, hspace = 0.4) # 通过hspace调整子图间距
plt.rcParams['font.family']=['SimHei'] # 显示中文
plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号
plt.subplot(211) # 绘制Hw幅度曲线
_ = plt.plot(w, np.abs(Hw))
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('omega')
plt.title('Amplitude Value:$|H(e^{jw})|$')
plt.grid()

plt.subplot(212) # 绘制Hw相位曲线
_ = plt.plot(w, np.angle(Hw))
xticks = np.array([-2*np.pi, -np.pi, 0, np.pi, 2*np.pi]) # 用于控制横坐标的显示范围
xlabels = ['$-2\pi$', '$-\pi$', '0', '$\pi$', '$2\pi$']
plt.xticks(xticks, xlabels)
plt.xlabel('omega')
plt.title('Phase Value:$\measuredangle X(e^{jw})$') # ∡
plt.grid()

plt.show()