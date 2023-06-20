clear all;
close all;
clc;
t=-3:0.001:3;
x1=xt(t);
x2=xt(-2*t);
x3=xt(t/2+1);
x4=5*xt(t)
subplot(4,1,1);
plot(t,x1);
grid on;
title('x(t)');
subplot(4,1,2);
plot(t,x2);
grid on;
title('x(-2t)');
subplot(4,1,3);
plot(t,x3);
grid on;
title('x(t/2+1)');
subplot(4,1,4);
plot(t,x4);
grid on;
title('5x(t)');
