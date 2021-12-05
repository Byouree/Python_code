def substring(str1,n):
    for i in range(n):
        for j in range(i+1,n+1):
            print(str[i:j])



str="ABCDE"
substring(str, len(str))
