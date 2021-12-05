def common_elements(l1,l2):
    common=[]
    count = 0
    for i in l1:
        for j in l2:
            if j == i:
                common.append(i)
                count +=1
    print("Iteration: ", common, "count: ", count)


def common_elements_dict(l1,l2):
    dict1={}
    for key in l2:
        dict1[key] = 1
    count=0
    for i in l1:
        if dict1.get(i) != None:
            print(i, end=" ")
            count +=1
    print()
    print("Common elements in both list is : ", count)

def common_elements_set(l1,l2):
    #set1 = set()
    set_l1 = set(l1)
    set_l2 = set(l2)
    set1 = set_l1 & set_l2
    print(list(set1))



l1=[2,4,6,8,10,12,14]
l2=[3,6,9,12,15,18]
#common_elements(l1,l2)
#common_elements_dict(l1,l2)
common_elements_set(l1,l2)
