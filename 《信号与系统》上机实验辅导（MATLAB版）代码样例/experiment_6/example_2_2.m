clear all;
close all;
clc;
syms s;
Xs=4*s/(s^2+5*s+6);
xt=ilaplace(Xs);
