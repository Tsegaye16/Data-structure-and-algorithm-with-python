def fibo(n):
    if n==0 or n==1:
        return  n
    else:
        return fibo(n-1)+fibo(n-2)


n=6
print(fibo(n))