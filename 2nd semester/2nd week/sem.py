# # def build_tree(a):
# #     n = len(a)
# #     tree = {}
# #     for i in range(n):
# #         tree[n + i] = a[i]
# #     for i in range(n - 1, 0, -1):
# #         tree[i] = tree[2 * i + 2] + tree[2 * i + 1]
# #     return tree
# #
# #
# # def sum_tree(tree, l, r):
# #     n = len(tree)
# #     _sum = 0
# #     l += n
# #     r += n
# #     while l < r:
# #         if (l & 1) > 0:
# #             _sum += tree[l]
# #             l += 1
# #         if (r & 1) > 0:
# #             r -= 1
# #             _sum += tree[r]
# #         l = l // 2
# #         r = r // 2
# #     return _sum
def mktree(a: list[int], lng: int) -> list:
    tree = [None] * (4 * lng)
    tree[0] = a
    for i in range(1, 4 * lng):
        if tree[i] is not None:
            continue
        if (i & 1) == 1:
            coretree = tree[(i - 1) // 2]
            if coretree is None or len(coretree) == 1:
                continue
            tree[i] = coretree[:len(coretree) // 2]
        else:
            coretree = tree[(i - 2) // 2]
            if coretree is None or len(coretree) == 1:
                continue
            tree[i] = coretree[len(coretree) // 2:]
    while tree[-1] is None:
        tree.pop()
    return tree

#
# def tree_w_max(tree: list[list[int]]) -> list[int]:
#     restree = [None] * len(tree)
#     for i in range(len(tree) - 1, -1, -1):
#         if tree[i] is None:
#             restree[i] = float('-inf')
#             continue
#         if len(tree[i]) == 1:
#             restree[i] = tree[i]
#             continue
#         a = restree[2 * i + 1]
#         b = restree[2 * i + 2]
#         if a >= b:
#             restree[i] = a
#         else:
#             restree[i] = b
#     return restree
#
#
# def find_otrezok(tree: list[list[int]], left: int, right: int) -> list[int]:
#     ar = tree[0]
#     seek = ar[left:right + 1]
#     inds = []
#     i = 1
#     while seek:
#         d = tree[i]
#         if d is not None and (set(d) & set(seek)) == set(d):
#             inds.append(i)
#             subseek = []
#             for x in seek:
#                 if x not in tree[i]:
#                     subseek.append(x)
#             seek = subseek
#         i += 1
#     return inds
#
#
tr = mktree([1, 2, 3, 4, 5], 5)
print(tr)