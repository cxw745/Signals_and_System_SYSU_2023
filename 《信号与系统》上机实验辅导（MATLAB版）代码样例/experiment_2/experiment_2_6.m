clear all;
close all;
clc;
k=0:50;
a=[1 0.95 0.9025];
b=[1/3 1/3 1/3];
c=[2 3];
d=[0 0];
h=impz(b,a,k);
u=[ones(1,length(k))];
g=filter(b,a,u);
figure(1);
subplot(2,1,1);
stem(k,h);
xlabel('n');
title('h:impulse response')
grid on;
subplot(2,1,2);
stem(k,g);
xlabel('n');
title('g:step response')
grid on;
figure(2);
x=cos(k*pi/3);
y1=filter(b,a,x);
subplot(3,1,1);
stem(k,y1);
xlabel('n');
title('yx:zero-sate response')
grid on;
z=filtic(b,a,c,d);
y2=filter(b,a,x,z);
subplot(3,1,2);
stem(k,y2);
xlabel('n');
title('ya:complete response')
grid on;
x1=zeros(1,length(k));
y3=filter(b,a,x1,z);%y3=y2-y1;
subplot(3,1,3);
stem(k,y3);
xlabel('n');
title('y0:zero-input response')
grid on;
