t=-2:0.001:2;
%N=input('N=');								% N为输入要达到的最高次谐波的次数
c0=0.5;
N1=50;
fN1=c0*ones(1,length(t));
for n=1:2:N1
fN1=fN1+cos(pi*n*t)*sinc(n/2);
end
subplot(3,1,1)
plot(t,fN1)
title('N=10')
axis([-2 2 -0.2 1.2]);
N2=100;
fN2=c0*ones(1,length(t));
for n=1:2:N2
fN2=fN2+cos(pi*n*t)*sinc(n/2);
end
subplot(3,1,2)
plot(t,fN2)
title('N=100')
axis([-2 2 -0.2 1.2]);
N3=1000;
fN3=c0*ones(1,length(t));
for n=1:2:N3
fN3=fN3+cos(pi*n*t)*sinc(n/2);
end
subplot(3,1,3)
plot(t,fN3)
title('N=1000')
axis([-2 2 -0.2 1.2]);
