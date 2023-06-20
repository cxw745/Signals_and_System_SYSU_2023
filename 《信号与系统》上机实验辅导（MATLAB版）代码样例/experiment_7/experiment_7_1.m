clear all;
close all;
clc;
b=[1 0.7 0.6];
a=[1 3.5 2];
subplot(2,1,1);
zplane(b,a);
grid on;
[h,w]=freqz(b,a);
subplot(2,1,2);
plot(w/pi,abs(h));
title('Magnitude Response');
grid on;