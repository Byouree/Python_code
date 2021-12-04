def last_word(A):
    arr = A.split(' ')
    size = len(arr)
    if size == 1:
        print(arr)
        print(A)
        return len(A)

    return len(arr[-1])



A = "Hellos"
print("Length of last word: ", last_word(A))
