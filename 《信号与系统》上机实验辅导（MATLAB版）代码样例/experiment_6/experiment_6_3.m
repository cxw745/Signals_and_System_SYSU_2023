clear all;
close all;
clc;
b=[1,-3,2];
a=[5,2,-7];
sys=tf(b,a);
pzmap(sys);
[p,z]=pzmap(sys);
sgrid;