list1=[4,7,9,2]
list1.reverse()
#print(list1)

list1=[4,7,9,2]
list2=list1[::-1]
#print(list2)


list3 = list(reversed(list1))
#print(list3)



list1=[4,7,9,2]
list2=[]
for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
print(list2)
