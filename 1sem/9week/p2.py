def stack_calc(s: str):
    s_list = list(s.split())
    stack = []
    for x in s_list:
        if x.isdigit():
            stack.append(int(x))
        match x:
            case '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            case '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            case '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            case '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(b / a)
    return int(stack[0])


print(stack_calc('2 3 - 12 10 - * 4 2 / +'))