function y=sawcos(t,n,w);
y=2*sawtooth(t*pi/2,0.5).*cos(n*w*t);