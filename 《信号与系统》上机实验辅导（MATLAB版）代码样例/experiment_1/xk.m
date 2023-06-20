function f=xk(k)
len=length(k);
for i=1:len
    if k(i)<-2
        x1(i)=-1;
    elseif k(i)>=-2 & k(i)<=1
        x1(i)=k(i);
    else
        x1(i)=1/k(i);%exp(-2*k(i));
    end
end
f=x1;
end