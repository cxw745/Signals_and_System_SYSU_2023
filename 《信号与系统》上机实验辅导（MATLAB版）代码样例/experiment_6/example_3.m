clear all;
close all;
clc;
num=conv([1,2],[1,-2]);
den=conv(conv([1,0],[1,3]),[1,1]);
[r,p,k]=residue(num,den);
r;
p;
k;
