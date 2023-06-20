clear all;
close all;
clc;
b=[1,-3,2];
a=[5,2,-7];
w=0:0.01:2;
s=j*w;
h=polyval(b,s)./polyval(a,s);
hm=abs(h);
hp=angle(h)*180/pi;
subplot(2,1,1);
plot(w,hm);
xlabel('w');
ylabel('Magnitude');
grid on;
subplot(2,1,2);
plot(w,hp);
xlabel('w');
ylabel('Phase');
grid on;
