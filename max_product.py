def maxpro(list1):
    global pair
    maxm=0
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]*list1[j]>maxm:
                maxm=list1[i]*list1[j]
                pair=str(list1[i])+" , "+str(list1[j])
    print("The number that have maximum product ",maxm)
    print("The pars are ",pair)

list1=[1, 4, 6, 8, 3, 5, 7, 2]
maxpro(list1)