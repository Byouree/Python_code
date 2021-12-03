def postfix_exp(A):
    operators=["+", "-", "*", "/"]
    size = len(A)
    stack = []

    for item in A:
        if item not in operators:
            stack.append(item)
        else:
            first = int(stack.pop())
            second = int(stack.pop())

            if item == "+":
                res = second + first
            elif item =="-":
                res = second - first
            elif item =="*":
                res = second * first
            elif item =="/":
                res = second / first
            stack.append(res)
    return stack[-1]

A = ["2", "1", "+", "3", "*"]
print(postfix_exp(A))
