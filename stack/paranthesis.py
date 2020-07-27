def ps(s):
    bracket = {"{":"}","(":")","[":"]"}
    
    stack = []

    for i in s:
        if i in bracket:
            stack.append(i)

        elif stack and bracket[stack[-1]] == i:
            stack.pop()

        else:
            return False
    return stack == []
print(ps("{}"))