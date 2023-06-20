clear all;
close all;
clc;
syms s;
Hs=(s-2)*(s-1)/(5*s^2+2*s+7);
ht=ilaplace(Hs);