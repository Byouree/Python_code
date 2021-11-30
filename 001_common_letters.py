def common_letters():
    str1=input("Enter the 1st string: ")
    str2 = input("Enter the 2nd string: ")
    s1 = set(str1)
    s2 = set(str2)
    li = s1 & s2
    print(li)

common_letters()
 
 
