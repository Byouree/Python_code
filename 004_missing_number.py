def get_missing_summation(a):
    n=a[-1]
    total = n*(n+1)//2
    sums = sum(a)
    print(total-sums)


def get_missing_xor(a):
    n = len(a)
    xor_a = a[0]
    for index in range(1, n):
        xor_a = xor_a^a[index]
    x2=0
    for index in range(1, n+2):
        x2=x2^index
    print(xor_a^x2)


a=[1,2,4,5,6,7]
get_missing_summation(a)
get_missing_xor(a)


