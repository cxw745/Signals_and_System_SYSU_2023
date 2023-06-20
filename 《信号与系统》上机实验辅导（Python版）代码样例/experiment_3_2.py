# 导入 需要的 library 库
import numpy as np  # 科学计算
import matplotlib.pyplot as plt  # 画图
import scipy.signal as sg  # 导入 scipy 的 signal 库 命名为 sg
# import control as ctrl  # 导入 conctrl 库 命名为 ctrl
import sympy  # 符号运算
from scipy.integrate import quad  # 用于求解定积分

import warnings
warnings.filterwarnings("ignore") # 去掉常规警告


def Rect(A, tao, T, t):
    # 周期矩形函数
    temp_t = abs(t)
    while(temp_t >= T):  # 将时间变量t转移到[0,T]区间上
        temp_t -= T
    return A if temp_t <= tao/2 or temp_t >= T-tao/2 else 0  # 返回区间[0,T]内的函数值


def aNt(N, A, omega, T, tao):
    # 周期矩形傅里叶级数有限项级数系数
    an = np.zeros(N+1)  # 系数an，三角形式
    bn = np.zeros(N+1)  # 系数bn，三角形式
    FuncA0 = lambda t : Rect(A, tao, T, t)*2/T # 用于计算a0
    an[0] = quad(FuncA0, -T/2, T/2)[0]  # 计算a0
    for n in range(1, N+1):
        def FuncA(t): return Rect(A, tao, T, t)*np.cos(n*omega*t)*2/T
        def FuncB(t): return Rect(A, tao, T, t)*np.sin(n*omega*t)*2/T
        an[n] = quad(FuncA, -T/2, T/2)[0]
        bn[n] = quad(FuncB, -T/2, T/2)[0]
    return an, bn  # 返回傅里叶系数，从0~N


def plotSquare(A, T, tao):
    # 绘制周期矩形信号
    tt = np.arange(-3*T, 3*T, 0.1)  # 采样序列，用于绘制波形
    rect = np.array([Rect(A, tao, T, t) for t in tt])  # 产生周期矩形信号
    plt.figure(figsize=(20, 5))  # 通过figsize调整图大小
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.plot(tt, rect)  # 绘制周期矩形信号
    # 横坐标间隔，使用变量"_"是防止matplotlib打印输出无用信息
    _ = plt.xticks(np.arange(-3*T, 4*T, step=1.0))
    plt.title('周期矩形信号', {'size': 18})  # 显示title
    _ = plt.xlabel("Time: 基波周期T=4,宽度τ=2", {'size': 18})
    plt.grid(True)  # 显示网格


def xNt(an, bn, omega, T, N, tao):
    # 周期矩形傅里叶级数有限项级数
    A0 = an[0]
    t = np.arange(-3*T, 3*T, 0.1)  # 时间采样序列
    fnt = A0/2  # 直流项，即a0/2
    for n in range(1, N+1):
        fnt = fnt + an[n]*np.cos(n*omega*t) + bn[n]*np.sin(n*omega*t)  # 傅里叶级数N项逼近值
    return fnt


def plot_xNt(an, bn, omega, T, N, tao):
    tt = np.arange(-3*T, 3*T, 0.1)  # 时间采样序列
    plt.figure(figsize=(20, 20))  # 通过figsize调整图大小
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
    plt.subplots_adjust(wspace=0.2, hspace=1.0)  # 子图间距调整
    plt.subplot((N+2)//2, 2, 1)  # 绘制周期矩形信号的子图
    plt.plot(tt, np.array([Rect(A, tao, T, t) for t in tt]))  # 绘制周期矩形信号
    _ = plt.xticks(np.arange(-3*T, 4*T, step=T))
    plt.title("周期矩形信号", {'size': 14})
    plt.grid(True)  # 显示网格
    plt.subplot((N+2)//2, 2, 2)  # 绘制周期矩形信号直流分量的子图
    plt.plot(tt, np.ones_like(tt)*an[0]/2)  # 绘制周期矩形信号直流分量
    _ = plt.xticks(np.arange(-3*T, 4*T, step=T))
    plt.title("周期矩形信号直流分量", {'size': 14})
    plt.grid(True)  # 显示网格
    for i in range(1, N+1):
        # 显示N=1~10项傅里叶级数逼近
        plt.subplot((N+2)//2, 2, i+2)  # 绘制周期矩形信号及其N项傅里叶级数逼近的子图
        plt.plot(tt, np.array([Rect(A, tao, T, t) for t in tt]))  # 绘制周期矩形信号
        plt.plot(tt, xNt(an, bn, omega, T, i, tao))  # N=i项傅里叶级数逼近
        _ = plt.xticks(np.arange(-3*T, 4*T, step=T))  # 横坐标间隔
        plt.title(f"周期矩形信号及其N={i}项傅里叶级数逼近", {'size': 14})
        plt.grid(True)  # 显示网格
    plt.show()  # 显示图像


T = 4  # 基波周期
tao = 2  # 宽度，即有效区间[-T1,T1],tao=2*T1
omega = 2*np.pi/T  # 基波频率
A = 1  # 幅度
N = 10  # N项有限项级数逼近，可修改N值显示不同的逼近效果
n = np.arange(0, N+1)  # 0~N傅里叶级数项数序列
an, bn = aNt(N, A, omega, T, tao)  # 0~N傅里叶级数幅度值

# 绘制周期矩形信号傅里叶级数三角形式幅值
fig, axs = plt.subplots(1, 2, figsize=(20, 5))  # 通过figsize调整图大小
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
plt.subplots_adjust(wspace=0.2, hspace=0)  # 通过wspace调整子图间距
plt.subplot(121)  # 绘制傅里叶三角级数cos项赋值的子图
plt.stem(n[1:], an[1:], use_line_collection=True)  # 傅里叶三角级数cos项赋值
plt.grid(True)  # 显示网格
plt.title('傅里叶三角级数cos项幅值', {'size': 14})  # 显示title
_ = plt.xlabel("傅里叶级数项数N", {'size': 14})
plt.subplot(122)  # 绘制傅里叶三角级数sin项赋值的子图
plt.stem(n[1:], bn[1:], use_line_collection=True)  # 傅里叶三角级数sin项赋值
plt.title('傅里叶三角级数sin项幅值', {'size': 14})  # 显示title
_ = plt.xlabel("傅里叶级数项数N", {'size': 14})
plt.grid(True)  # 显示网格
plt.show()  # 显示图像

# 有限项级数逼近
plot_xNt(an, bn, omega, T, N, tao)
