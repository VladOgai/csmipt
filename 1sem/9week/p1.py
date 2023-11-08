# только в прямую
# 1
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def print_tree(self):
        print(self.val, end=' ')
        if self.left is not None:
            self.left.print_tree()
        if self.right is not None:
            self.right.print_tree()


def parser(s: str) -> list:
    res = ['']
    for let in s:
        if let == ' ':
            continue
        if let.isdigit():
            if isinstance(res[-1], int):
                res[-1] = int(str(res[-1]) + let)
            else:
                res.append(int(let))
        else:
            res.append(let)
    res = res[1:]
    res.append('end')
    return res


def get_el(el_list: list, exp) -> bool:
    if el_list[0] == exp:
        del el_list[0]
        return True
    return False


def get_number(el_list: list):
    if get_el(el_list, '('):
        el = get_sumdif(el_list)
        get_el(el_list, ')')
        return el
    el = el_list[0]
    if isinstance(el, int):
        el_list[0:1] = []
        return Tree(el, None, None)
    return None


def get_multdiv(el_list: list):
    a = get_number(el_list)
    if get_el(el_list, '*'):
        b = get_multdiv(el_list)
        return Tree('*', a, b)
    if get_el(el_list, '/'):
        b = get_multdiv(el_list)
        return Tree('/', a, b)
    return a


def get_sumdif(el_list: list):
    a = get_multdiv(el_list)
    if get_el(el_list, '+'):
        b = get_sumdif(el_list)
        return Tree('+', a, b)
    if get_el(el_list, '-'):
        b = get_sumdif(el_list)
        return Tree('-', a, b)
    return a


def print_pol(s: str):
    s_list = parser(s)
    s_tree = get_sumdif(s_list)
    s_tree.print_tree()


print_pol('(3 + 4 * (2 - 1)) / 5')  # / + 3 * 4 - 2 1 5
