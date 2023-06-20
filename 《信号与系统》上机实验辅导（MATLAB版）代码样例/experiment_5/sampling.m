function fz=sampling(fy,fs)
fs0=1000;
tp=1.0;
t=[-tp:1/fs0:tp];
k1=0:999; 
k2=-999:-1;
m1=length(k1); 
m2=length(k2); 
f=[fs0*k2/m2,fs0*k1/m1]; 
w=[-2*pi*k2/m2,2*pi*k1/m1];%����ȡ����Ľ�Ƶ�� 
fx1=eval(fy);%fx1��ʾ��fy�ź���ȡ����ֵ
FX1=fx1*exp(-j*[1:length(fx1)]'*w);%����DTFT������ɢʱ���źŵ�Ƶ�׼���
figure(1) 
subplot(2,1,1);
plot(t,fx1,'r'); 
title('ԭ�ź�');
xlabel('ʱ��t (s)');
axis([min(t),max(t),min(fx1),max(fx1)]);
subplot(2,1,2),plot(f,abs(FX1),'r');
title('ԭ�źŷ���Ƶ��');
xlabel('Ƶ��f (Hz)');
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
title('ȡ���ź�');
xlabel('ʱ��t (s)');
line([min(t),max(t)],[0,0]);
subplot(2,1,2);
plot(f1,abs(FZ),'m');
title('ȡ���źŷ���Ƶ��');
xlabel('Ƶ��f (Hz)');
end