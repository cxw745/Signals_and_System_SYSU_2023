%---Experiment of Laplace Transform
% ---------Laplace Transform of the input signal--------
syms t s;
x = exp(-3*t) * heaviside(t);
figure(1),subplot(2,1,1),ezplot(t,x);
grid on;
xlabel('t');
ylabel('x(t)');
title('The Input Signal');
X_s = laplace(x, s);
figure(1),subplot(2,1,2),ezplot(s, X_s);
grid on;
xlabel('s');
ylabel('L(s)');
title('The LT of The Input Signal');

%---------------Zero State Response----------------
Ys_ZS = (2*s*X_s+X_s)/(s^2 + 3 * s + 2)
y_Zs = ilaplace(Ys_ZS);
figure(2),subplot(2,1,1),ezplot(s,Ys_ZS);
grid on;
xlabel('s');
ylabel('Ys_Zs');
title('The LT of the Zero State Response');

figure(2),subplot(2,1,2),ezplot(t,y_Zs);
grid on;
xlabel('t');
ylabel('y_Zs');
title('The  Zero State Response');

%---------------Zero Input Response----------------
Ys_Zin = (2*s + 7)/(s^2 + 3 * s + 2)
y_Zin = ilaplace (Ys_Zin);
figure(3),subplot(2,1,1),ezplot(s,Ys_Zin);
grid on;
xlabel('s');
ylabel('Ys_Zin');
title('The LT of the Zero Input Response');

figure(3),subplot(2,1,2),ezplot(t,y_Zin);
grid on;
xlabel('t');
ylabel('y_Zin');
title('The  Zero Input Response');

%---------------Total Response----------------
y = y_Zin + y_Zs;

figure(4),subplot(3,1,2),ezplot(t,y_Zin);
grid on;
xlabel('t');
ylabel('y_Zin');
title('The  Zero Input Response');

figure(4),subplot(3,1,1),ezplot(t,y_Zs);
grid on;
xlabel('t');
ylabel('y_Zs');
title('The  Zero State Response');

figure(4),subplot(3,1,3),ezplot(t,y);
grid on;
xlabel('t');
ylabel('y');
title('The Total Response');



