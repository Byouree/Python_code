def reverse(str):
    print(str)
    str = str.split(" ")
    print(str)
    print(str[::-1])
    rev_set = str[::-1]
    new_set = " ".join(rev_set)
    print(new_set)
str = "ABC is online platform"
reverse(str)
