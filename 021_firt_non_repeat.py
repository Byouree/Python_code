def first_non_repeat(str):
    str = list(str)
    dic1 = {}
    print(str)

    for key in str:
        if key not in dic1:
            dic1[key] = 1

        else:
            print("repeat: " , key)
            dic1[key] += 1
    print(dic1)

    for index in range(len(str)):
        if dic1[str[index]] == 1:
            return index, str[index]



    """
    for key, value in dic1.items():
        if value == 1:
            return key
    """

str = "NZETSOENTST"
print(first_non_repeat(str))
