%f1='(sinc(2*20*pi*t)+2*sinc(2*10*pi*t)).*(heaviside(t+0.1)-heaviside(t-0.1))';
f1='(1+cos(2*20*pi*t)/2).*(heaviside(t+1.0)-heaviside(t-1.0))'
fs0=sampling(f1,30); %欠采样
fr0=reconstruct(fs0,30);  
pause;
fs1=sampling(f1,40);%临 界采样
fr1=reconstruct(fs1,40);  
pause;
fs2=sampling(f1,100);%过采样 
fr2=reconstruct(fs2,100);
clear all;
clc;