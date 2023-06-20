clear all;
close all;
clc;
kh=0:8;
kx=0:6;
h = [3 2 1 -2 1 0 -4 0 3]; % impulse response
x = [1 -2 3 -4 3 2 1]; % input sequence
y = conv(x,h);
n = 0:(length(h)+length(x)-2);%
subplot(2,2,1);
stem(kx,x);
grid on;
title('x[k]');
subplot(2,2,2);
stem(kh,h);
grid on;
title('h[k]');
subplot(2,1,2);
stem(n,y);
grid on;
title('x[k]*h[k]');
