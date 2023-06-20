clear all;
close all;
clc;
k=0:20;
a=[1 0.25 0.5];
b=[1 1 0];
c=[-2 3];
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
x=(1/2).^k;
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
title('yx:complete response')
grid on;
z=filtic(b,a,c,d);
x1=zeros(1,length(k));
y3=filter(b,a,x1,z);
subplot(3,1,3);
stem(k,y3);
xlabel('n');
title('yx:zero-input response')
grid on;
