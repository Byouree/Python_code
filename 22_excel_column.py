def exceltitle_num(str):
    size = len(str)
    result = 0
    for i in range(size):
        print("i size", i,size)

        num = ord(str[i])-ord('A')+1
        result += num*pow(26, size-1)
        size-=1
        print("size-1 ",size)
        print(result)
    return result




str = "ABC"
print(exceltitle_num(str))
