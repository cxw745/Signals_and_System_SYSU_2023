clear all;
close all;
clc;
syms t w;
X=fourier(exp(-2*abs(t)));
figure(1);
subplot(2,1,1);
ezplot(X);
xlabel('Xw')
grid on;
Y=X*X;
subplot(2,1,2);
ezplot(Y);
xlabel('Yw');
grid on;
y=ifourier(Y,t);
figure(2)
subplot(2,1,1);
ezplot(y);
grid on;


