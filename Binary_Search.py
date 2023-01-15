def binary(list1,item):
    first=0
    last=len(list1)-1
    while first<=last:
        mid=(first+last)//2
        if list1[mid]>item:
            last=mid-1

        elif list1[mid]<item:
            first=mid+1
        else:
            if list1[mid]==list1[mid-1]:
                return mid-1
            else:
                return mid
    return None