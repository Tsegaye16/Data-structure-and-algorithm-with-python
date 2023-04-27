#<<<<<<< HEAD
def Linear_Search(list1,value):
    list2=[]
    flag=True
    for i in range(len(list1)):
        if value==list1[i]:
            flag=False
            list2.append(i)


    if flag==False:
        print("The value is found at the index of :")
        for j in list2:
            print(j,end=" ")


n=int(input("enter the lenght of the list you enter"))
list3=[]
for i in range(n):
    k=int(input())
    list3.append(k)

value=int(input("enter the value you went to find"))

Linear_Search(list3,value)
#=======
def Linear_Search(list1, value):
    list2 = []
    flag = True
    for i in range(len(list1)):
        if value == list1[i]:
            flag = False
            list2.append(i)

    if flag == False:
        print("The value is found at the index of :")
        for j in list2:
            print(j, end=" ")


n = int(input("enter the lenght of the list you enter"))
list3 = []
for i in range(n):
    k = int(input())
    list3.append(k)

value = int(input("enter the value you went to find"))

Linear_Search(list3, value)
#>>>>>>> c5c997cd7e2a8429e9c67f395d1859a11859a00c
