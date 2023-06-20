function fz=sampling(fy,fs)
fs0=1000;
tp=1.0;
t=[-tp:1/fs0:tp];
k1=0:999; 
k2=-999:-1;
m1=length(k1); 
m2=length(k2); 
f=[fs0*k2/m2,fs0*k1/m1]; 
w=[-2*pi*k2/m2,2*pi*k1/m1];%求解出取样点的角频率 
fx1=eval(fy);%fx1表示从fy信号中取样的值
FX1=fx1*exp(-j*[1:length(fx1)]'*w);%利用DTFT进行离散时间信号的频谱计算
figure(1) 
subplot(2,1,1);
plot(t,fx1,'r'); 
title('原信号');
xlabel('时间t (s)');
axis([min(t),max(t),min(fx1),max(fx1)]);
subplot(2,1,2),plot(f,abs(FX1),'r');
title('原信号幅度频谱');
xlabel('频率f (Hz)');
axis([-100,100,0,max(abs(FX1))+5]);
Ts=1/fs;
t1=-tp:Ts:tp; 
f1=[fs*k2/m2,fs*k1/m1]; 
t=t1; 
fz=eval(fy); 
FZ=fz*exp(-j*[1:length(fz)]'*w);
figure(2);
subplot(2,1,1);
stem(t,fz,'.');
title('取样信号');
xlabel('时间t (s)');
line([min(t),max(t)],[0,0]);
subplot(2,1,2);
plot(f1,abs(FZ),'m');
title('取样信号幅度频谱');
xlabel('频率f (Hz)');
end