class solution:
    def merge_sort(self,list1):
        #list1 = [4, 2, 9, 0, 5, 9, 1, 8]
        if len(list1)>1:
            mid=len(list1)//2
            left_list=list1[:mid]
            right_list=list1[mid:]


            self.merge_sort(left_list)
            self.merge_sort(right_list)


            i=j=k=0
            while i<len(left_list) and j<len(right_list):
                if left_list[i]<right_list[j]:
                    list1[k]=left_list[i]
                    i+=1
                else:
                    list1[k]=right_list[j]
                    j+=1
                k+=1
            while i<len(left_list):
                list1[k]=left_list[i]
                i+=1
                k+=1
            while j<len(right_list):
                list1[k]=right_list[j]
                j+=1
                k+=1
        return list1


list2 = [4, 2, 9, 0, 5, 9, 1, 8]
defd =solution()
print(defd.merge_sort(list2))
#print(list1)