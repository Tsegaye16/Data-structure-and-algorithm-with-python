def pre(list1 ):
    pr=""
    n=min(len(i )for i in list1)
    m=max(len(i )for i in list1)
    list1=sorted(list1)
    # for i in list1:
    #     if len(i)>n:
    #         for n in range(m-n):
    #             i.pop()
    for i in range(n):
        if list1[0][i]==list1[-1][i]:
            pr=pr+list1[0][i]
    print(pr)






list1=["flower","flow","flight"]
pre(list1)