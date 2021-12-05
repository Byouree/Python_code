dict1 = {1:'apple', 2:'banana'}
dict2 = {3:'orange', 4:'berry'}

dict1.update(dict2)
#print(dict1)
#print(dict2)

dict3={**dict1, **dict2}
print(dict3)


