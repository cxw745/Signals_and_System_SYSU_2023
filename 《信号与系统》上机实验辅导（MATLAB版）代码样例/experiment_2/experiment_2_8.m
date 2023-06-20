clear all;
close all;
clc;
syms t n;
T=4;
tao=2;
%A=2*sawtooth(t*pi/2,0.5);
x=abs(t)*exp(-j*n*2*pi/T*t);
Xn=int(x,t,-tao/2,tao/2)/T;
Xn=simple(Xn);Xn
n=[-20:1,0,1:20];
Xn=subs(Xn,'n',n);
stem(n,Xn);
title('Xn');
grid on;
