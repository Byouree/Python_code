a = list(map(int, input().split(' ')))

ascending = True
descending = True
print(a)
for i in range(len(a)-1):
    if a[i+1] - a[i] > 0:
        descending = False
    elif a[i+1] - a[i] < 0:
        ascending = False

if ascending:
    print("ascending")
elif descending:
    print("descending")
else:
    print("mixed")



        
