arr = [1,4,2,5,2,3,4,1,4,5,2,3]

#set
def remove_duplicate_set(arr):
    set_arr = list(set(arr))
    print(set_arr)

#array
def remove_dup_arr(arr):
    tmp=[]
    for i in arr:
        if i not in tmp:
            tmp.append(i)
    print(tmp)

#Lambda
remove_duplicate_func=lambda arr:list(set(arr))
print(remove_duplicate_func(arr))

dict1 = {
    'car':["Ford","Toyota", "Ford","Toyota"],
    'brand':["Mustang", "Ranz","Mustang", "Ranz"]

}

dict2 = {}

for key, value in dict1.items():
    dict2[key] = set(value)
print(dict2)



arr = [1, 4, 2, 5, 2, 3, 4, 1, 4, 5, 2, 3]
remove_duplicate_set(arr)
remove_dup_arr(arr)
