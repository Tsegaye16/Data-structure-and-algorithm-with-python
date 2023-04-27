def dval(list1,target):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[j]+list1[i]==target:
                print(list1[i],list1[j])


list1=[1, 3, 6, 2, 9, 4]
target = 6
dval(list1,target)