def smal(list1):
    ans = []
    f=[]
    coun = 0
    for i in range(len(list1)):
        ans.append(list1[i])
        list1.remove(list1[i])
        list3=list1
        for j in range(len(list3)):
            if list3[j]<ans[0]:
                coun=coun+1
        f.append(coun)
        ans.pop()
    return f
list1=[5,2,6,1]
print(smal(list1))




