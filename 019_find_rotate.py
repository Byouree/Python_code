"""
def rotate(str):
    n = len(str)
    for i in range(n):
        #print(str[i:])
        #print(str[0:i])
        print(str[i:]+str[0:i])
"""

def rotate(str):
    n = len(str)
    tmp=str+str
    for i in range(n):
        for j in range(n):
            print(tmp[i+j], end="")
        print()

str = "ABCD"
rotate(str)
