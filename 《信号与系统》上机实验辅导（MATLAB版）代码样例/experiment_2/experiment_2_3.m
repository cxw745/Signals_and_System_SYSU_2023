T=4;
tao=2;
w=2*pi/T;
a0=quadl(@singrect,-2,2)/T; % ����a0 
N=10; 
an=zeros(1,N);
bn=zeros(1,N);
for k=1:N
an(k)=quadl(@rectcos, -2, 2, [], [], k, w)*2/T;
% ����an. quadl�е�[], []��ʾ��Ĭ�Ͼ��Ƚ�����ֵ����
% rectcos�����еĺ���������;
bn(k)=quadl(@rectsin, -2, 2, [], [], k, w)*2/T; %����bn;
end;
n=1:1:N;
figure(1);
subplot(1,2,1);plot(n, an, '-o');grid on;
subplot(1,2,2);plot(n, bn, '-o');grid on;
t=-6:0.01:6;
x=pulstran(t,-8:4:8,'rectpuls',2); %�������ھ��������ź� 
figure(2);subplot(6,2,1);
plot(t, x);
axis([-8,8,-1,2]); grid on;
% ��������ƽ� 
A0=a0;
AN=sqrt(an.^2+bn.^2);
fiN=-atan(bn./an);
subplot(6,2,2); plot(t,A0/2); grid on; %ֱ���� 
wave=a0/2;
for k=1:10
wave=wave+an(k)*cos(k*w*t+fiN(k));
subplot(6,2,k+2);plot(t,wave);grid on;
end
