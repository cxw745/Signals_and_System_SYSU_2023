clear all;
close all;
clc;
fs=1000;
t=-1.1:1/fs:2.1;
x11=(t>=0);%定义阶跃函数
x12=exp(-3*t).*(t>=0);
y1=conv(double(x11),double(x12))/fs;
n=length(y1);
tt=(0:n-1)/fs-2.2;%定义新序列时间范围
subplot(2,2,1);
plot(t,x11);
grid on;
title('x1');
subplot(2,2,2);
plot(t,x12);
title('x2');
subplot(2,1,2);
plot(tt,y1);
grid on;
title('conv(x1,x2)');
