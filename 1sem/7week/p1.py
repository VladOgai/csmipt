class Vector:
    def __init__(self, x, y, z):
        assert isinstance(x, float) or isinstance(x, int) and isinstance(y, float) or isinstance(y, int) and isinstance(
            z, float) or isinstance(z, int)
        self.__x, self.__y, self.__z = x, y, z

    def __abs__(self):
        return (self.__x ** 2 + self.__y ** 2 + self.__z ** 2) ** 0.5

    def __add__(self, other):
        return Vector(self.__x + other.__x, self.__y + other.__y, self.__z + other.__z)

    def __sub__(self, other):
        return Vector(self.__x - other.__x, self.__y - other.__y, self.__z - other.__z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.__x * other.__x + self.__y * other.__y + self.__z * other.__z
        if isinstance(other, float):
            return Vector(other * self.__x, other * self.__y, other * self.__z)

    def __rmul__(self, other):
        if isinstance(other, float):
            return Vector(other * self.__x, other * self.__y, other * self.__z)

    def get_cords(self):
        return self.__x, self.__y, self.__z


def mass_centre(dots: list) -> tuple:
    s_vector = Vector(0, 0, 0)
    for dot in dots:
        s_vector = s_vector + Vector(*dot)
    s_vector = s_vector * (1 / len(dots))
    return s_vector.get_cords()


def find_area(dot1, dot2, dot3):
    dd1, dd2, dd3 = Vector(*dot1), Vector(*dot2), Vector(*dot3)
    d1, d2, d3 = abs(dd1 - dd2), abs(dd2 - dd3), abs(dd1 - dd3)
    if (d1 + d2 > d3) and (d1 + d3 > d2) and (d2 + d3 > d1):
        area = ((d1 + d2 + d3) * (d1 + d2) * (d2 + d3) * (d1 + d3)) ** 0.5
        return area
    return 0


# 1.1
list_of_dots = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(mass_centre(list_of_dots))

# 1.2
list_of_dots2 = [(34, 48, 13), (43, 90, 90), (20, 6, 12), (31, 65, 98), (14, 62, 39), (7, 33, 52), (47, 66, 8),
                 (33, 23, 74), (90, 29, 70), (24, 33, 26)]
ss = 0
for i in range(len(list_of_dots2)):
    for j in range(i + 1, len(list_of_dots2)):
        for k in range(j + 1, len(list_of_dots2)):
            ss = max(ss, find_area(list_of_dots2[i], list_of_dots2[j], list_of_dots2[k]))
print(ss)
