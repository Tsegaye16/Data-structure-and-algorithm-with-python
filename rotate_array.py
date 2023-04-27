def sor(list1,target):
    first=0
    last=len(list1)-1
    while first<last:
        if list1[first]+list1[last]==target:
            return [first+1,last+1]
        if list1[first]+list1[last]>target:
            last-=1
        else:
            first+=1
    return []

list1=[0,1,2,3,4]
target=3
print(sor(list1,target))





