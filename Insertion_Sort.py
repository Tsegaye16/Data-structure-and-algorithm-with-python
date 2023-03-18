def insertion(list1):
    for i in range(1,len(list1)):
        current=list1[i]
        for j in range(i-1,len(list1)):
            list1[j+1]=list1[j]
        list1[i+1]=current





    return list1




list1=[2,6,8,2,4]
print(insertion(list1))