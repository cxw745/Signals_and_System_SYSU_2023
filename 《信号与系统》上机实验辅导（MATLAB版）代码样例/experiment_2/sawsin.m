function y=sawsin(t,n,w);
y=2*sawtooth(t*pi/2,0.5).*sin(n*w*t); % 定义了矩形脉冲与正弦函数的乘积 