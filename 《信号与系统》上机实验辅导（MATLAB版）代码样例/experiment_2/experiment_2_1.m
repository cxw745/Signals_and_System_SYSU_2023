clear all;
close all;
clc;
a=[1 4 4];
b=[1 3];
c=[1,-3];
sys1=tf(b,a);
[A B C D]=tf2ss(b,a);
sys=ss(A,B,C,D);%take care :sys1=sys
td=0.01;
t=0:td:10;
x=exp(-t).*(t>=0);
y1=lsim(sys1,x,t);
y2=lsim(sys,x,t,c);
y3=y2-y1;
figure(1);
h=impulse(sys1,t);
subplot(2,1,1)
plot(t,h);
xlabel('t(sec)');
title('h:impulse response');
grid on;
g=step(sys1,t);
subplot(2,1,2)
plot(t,g);
xlabel('t(sec)');
title('g:step response');
grid on;
figure(2);
subplot(3,1,1)
plot(t,y1);
xlabel('t(sec)');
title('yx:zero-state response');
grid on;
subplot(3,1,2)
plot(t,y2);
xlabel('t(sec)');
title('ya:complete response');
grid on;
subplot(3,1,3)
plot(t,y3);
xlabel('t(sec)');
title('y0:zero-input response');
grid on;
