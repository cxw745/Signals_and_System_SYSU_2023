clear;clc;
fs=8000;		%抽样频率
f=[523.25 523.25 587.33 392 349.23 349.23 293.66 392]; 
%各个乐音对应的频率
time=fs*[1/2,1/4,1/4,1,1/2,1/4,1/4,1];	%各个乐音的抽样点数
N=length(time);	%这段音乐的总抽样点数
east=zeros(1,N);	%用east向量来储存抽样点
n=1;
for num=1:N		%利用循环产生抽样数据，num表示乐音编号
    t=1/fs:1/fs:time(num)/fs;	%产生第num个乐音的抽样点
east(n:n+time(num)-1)=sin(2*pi*f(num)*t);		
%抽样点对应的幅值
    n=n+time(num);
end
sound(east,8000);		%播放音乐
