clear;clc;
fs=8000;		%����Ƶ��
f=[523.25 523.25 587.33 392 349.23 349.23 293.66 392]; 
%����������Ӧ��Ƶ��
time=fs*[1/2,1/4,1/4,1,1/2,1/4,1/4,1];	%���������ĳ�������
N=length(time);	%������ֵ��ܳ�������
east=zeros(1,N);	%��east���������������
n=1;
for num=1:N		%����ѭ�������������ݣ�num��ʾ�������
    t=1/fs:1/fs:time(num)/fs;	%������num�������ĳ�����
    G=zeros(1,time(num)); 		%GΪ�洢�������ݵ�����
G(1:time(num))=exp(1:(-1/time(num)):1/8000);		
%���������
    east(n:n+time(num)-1)=sin(2*pi*f(num)*t).*G(1:time(num));
 								%����num���������ϰ���
    n=n+time(num);
end
sound(east,8000);			%����
plot(east);

