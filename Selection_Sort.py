def selection(list1):
    for i in range(len(list1)):
        small = i
        for j in range(i + 1, len(list1)):
            # print(list1, list1[i], list1[j])
            if list1[small] > list1[j]:
                small = j
        print("*****************************")
        print(list1)
        print("Swapping to: ")
        list1[i], list1[small] = list1[small], list1[i]
        print(list1)
        print("*****************************")


list1 = [34, 22, 10, 19, 17]
selection(list1)
