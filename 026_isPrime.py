from math import sqrt
def prime_num(num):
    if num>1:
        for i in range(2, int(sqrt(num) + 1)):  #O(sqrt(num))
        #for i in range(2, int(num/2)):  #O(num/2)
        #for i in range(2, num): #O(num)
            if num%i==0:
                return False
        return True

is_prime=prime_num(23)
if is_prime:
    print("Prime number")
else:
    print("None prime number")
