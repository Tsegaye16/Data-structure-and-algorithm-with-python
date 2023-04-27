def bubble(list1):
    for i in range(len(list1)):
        for j in range(len(list1)-1):
            print(list1,list1[j],list1[j+1])
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
        print("One pass")

    print(list1)

list1=[45,37 ,29,8]
bubble(list1)

