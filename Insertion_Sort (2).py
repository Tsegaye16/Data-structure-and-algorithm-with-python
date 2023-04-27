#<<<<<<< HEAD
def insertion_sort(list1):
    for i in range(1,len(list1)):
        j=i
        while list1[j-1]>list1[j] and j>0:
            list1[j-1],list1[j]=list1[j],list1[j-1]
            j-=1


list1=[3,5,2,0,7,9,4]
insertion_sort(list1)
print(list1)
#=======
def insertion(list1):
    for i in range(1,len(list1)):
        current=list1[i]
        for j in range(i-1,len(list1)):
            list1[j+1]=list1[j]
        list1[i+1]=current





    return list1




list1=[2,6,8,2,4]
print(insertion(list1))
#>>>>>>> c5c997cd7e2a8429e9c67f395d1859a11859a00c
