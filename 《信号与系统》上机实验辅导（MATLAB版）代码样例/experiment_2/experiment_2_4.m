clear all;
close all;
clc;
syms t n;
T=4;
tao=2;
A=1;
x=A*exp(-j*n*2*pi/T*t);
Xn=int(x,t,-tao/2,tao/2)/T;
Xn=simple(Xn);Xn
n=[-20:20];
Xn=subs(Xn,'n',n);
stem(n,Xn);
title('Xn');
grid on;
