# Реализуйте структуру данных для эффективного вычисления индекса k-го слева нулевого элемента в отрезке массива.
# Входные данные
# В первой строке вводится одно натуральное число N (1 ≤ N ≤ 100000) — количество чисел в массиве. Во второй строке
# вводятся N чисел от 0 до 100000 — элементы массива. В третьей строке вводится одно натуральное число M (1 ≤ M ≤ 30000)
# — количество запросов на вычисление количества нулей. В следующих M строках вводится по три числа — номера левого и
# правого элементов отрезка массива (считается, что элементы массива нумеруются с единицы) и число k (1 ≤ k ≤ N).
# Выходные данные
# Для каждого запроса выведите индекс элемента массива, который является k-м слева нулевым элементом на соответствующем
# участке массива. Числа выводите в одну строку через пробел.


def maketable(arr: list[int], lng: int) -> list[int]:
    index_zero = 0
    for i in range(lng):
        if arr[i] == 0:
            arr[i] = [arr[i], index_zero]
            index_zero += 1
    index_previos_zero = None
    list_index_zeros = []
    for i in range(lng - 1, -1, -1):
        if isinstance(arr[i], list):
            index_previos_zero = i
            list_index_zeros.append(i)
        else:
            arr[i] = index_previos_zero
    list_index_zeros.reverse()
    return list_index_zeros


def find_k_zero(arr: list[int], left, k, table) -> int or None:
    if isinstance(arr[left], list):
        index_need_z = arr[left][1]
    elif arr[left] is None:
        index_need_z = None
    else:
        index_need_z = arr[arr[left]][1]
    if index_need_z is not None and (k - 1 + index_need_z) < len(table):
        return table[k - 1 + index_need_z]
    return None


n = int(input())
massiv = list(map(int, input().split()))
m = int(input())
tt = maketable(massiv, n)
reslist = []
for _ in range(m):
    l, r, k = map(int, input().split())
    l -= 1
    reslist.append(find_k_zero(massiv, l, k, tt))
print(*reslist)