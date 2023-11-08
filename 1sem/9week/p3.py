def obr_pol(expression: str) -> str:
    expression = expression.replace(' ', '')
    stack = []
    output = ''
    funcs = {'+': 1, '-': 0, '/': 2, '*': 3}
    for s in expression:
        if s.isdigit():
            output += s
        elif s in funcs.keys():
            while len(stack) and stack[-1] in funcs.keys() and funcs[stack[-1]] > funcs[s]:
                output += stack.pop()
            stack.append(s)
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack[-1] != '(':
                output += stack.pop()
            stack.pop()
    while len(stack):
        output += stack.pop()
    return output


exp = '1 + 2 * 3 - 4'
print(obr_pol(exp))
