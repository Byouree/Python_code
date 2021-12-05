def anagram(A):
    if A==None:
        return
    else:
        dict={}
        print(A)
        for i in range(len(A)):
            word=''.join(sorted(A[i]))
            print(word)
            if word not in dict:
                dict[word] = [i+1]
            else:
                dict[word].append(i+1)
        print(dict)

A=["cat","dog","god","tca","act"]
anagram(A)

