def fibo(n):
    first=0
    second = 1
    list1=[first,second]
    for i in range(n-2):
        third=first+second
        list1.append(third)
        temp=second
        first=temp
        second=third
    return list1

print(fibo(10))

