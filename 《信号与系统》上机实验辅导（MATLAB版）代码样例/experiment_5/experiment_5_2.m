f1='sinc(20*pi*t)+sinc(10*pi*t).*(heaviside(t+1.0)-heaviside(t-1.0))';
%f1='sin(2*pi*60*t)+cos(2*pi*25*t)+cos(2*pi*30*t)';
fs0=sampling(f1,40); %Ƿ����
fr0=reconstruct(fs0,40);  
fs1=sampling(f1,80);%�� �����
fr1=reconstruct(fs1,80);  
fs2=sampling(f1,100);%������ 
fr2=reconstruct(fs2,100);
clear all;
clc;