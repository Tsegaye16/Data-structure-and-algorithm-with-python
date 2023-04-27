def unique(list1):
    flag=True
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]==list1[j]:
                flag=False
            else:
                flag=True
    if flag==True:
        print("The list element is unique")
    else:
        print("The list element is not uniqe")


list1=[1, 7, 5, 6, 8]
unique(list1)