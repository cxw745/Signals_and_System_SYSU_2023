clear all;
close all;
clc;
syms t;
Xw=fourier(exp(-2*abs(t)));
subplot(2,2,2);
ezplot(Xw);
title('傅里叶变换X(w)')
grid on;
X1=fourier(exp(-2*abs(3*t)));
subplot(2,2,4);
ezplot(X1);
title('尺度变换X1(w)')
grid on;
t=-2.5:0.01:2.5;
x=exp(-2*abs(t));
x1=exp(-2*abs(3*t));
x=subs(x,'t',t);
x1=subs(x,'t',t);
subplot(2,2,1);
plot(t,x);
xlabel('t');
title('x(t)');
grid on;
subplot(2,2,3);
plot(t,x1);
xlabel('t');
title('x(3t)');
grid on;
