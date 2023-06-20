clear all;
close all;
clc;
syms s;
Xs=s/(2*s^2+3*s+1);
xt=ilaplace(Xs);
