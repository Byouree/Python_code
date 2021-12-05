arr = [1,4,2,5,2,3,4,1,4,5,2,3]

#set
#print(set(arr))

arr = [1,4,2,5,2,3,4,1,4,5,2,3]
#array
new_arr=[]
for i in range(len(arr)):
    if arr[i] not in new_arr:
        new_arr.append(arr[i])
#rint(new_arr)


#lambda
rem_duplicate_fun = lambda arr:set(arr)
print(rem_duplicate_fun(arr))


##dict
dict1 = {
    'car': ["Ford","Toyata","Ford","Toyata"],
    'brand': ["Mustang", "Ranz","Mustang", "Ranz"]
}

dict2={}

for key, value in dict1.items():
    dict2[key] = set(value)

print(dict2)
