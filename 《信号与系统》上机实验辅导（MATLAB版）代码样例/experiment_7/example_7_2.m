clear all;
close all;
clc;
syms n z;
Xz=z^3/(z-1)^3;
xn=iztrans(Xz,z,n);