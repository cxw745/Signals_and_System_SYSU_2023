clear all;
close all;
clc;
syms t s;
xt=heaviside(t-2);
Xs=laplace(xt,t,s);
Xs;