if __name__ == '__main__':
    e = int(input())
    edgelist = []
    vertices = set()
    for _ in range(e):
        a, b = map(int, input().split())
        edgelist.append((a, b))
        vertices.add(a)
        vertices.add(b)
    for a, b in edgelist:
        if b in vertices:
            vertices.remove(b)
    print(len(vertices))