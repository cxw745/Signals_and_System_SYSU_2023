clear all;
close all;
clc;
b=[2,10,2,5];
a=[2,4,7,11,6];
sys=tf(b,a);
pzmap(sys);
[p,z]=pzmap(sys);
sgrid;