n, m = map(int, input().split())
muzhiki_kotorie_ne_hotyat_zhit_vmeste = [{i} for i in range(1, n + 1)]
for _ in range(m):
    para = tuple(map(int, input().split()))
    muzhiki_kotorie_ne_hotyat_zhit_vmeste[para[0] - 1].add(para[1])
    muzhiki_kotorie_ne_hotyat_zhit_vmeste[para[1] - 1].add(para[0])
teams = set()
candidati = {i for i in range(1, n + 1)}
for h in range(n):
    for p in range(h + 1, n):
        if (p + 1) in muzhiki_kotorie_ne_hotyat_zhit_vmeste[h]:
            continue
        for z in range(p + 2, n + 1):
            if z in (candidati - (muzhiki_kotorie_ne_hotyat_zhit_vmeste[h] | muzhiki_kotorie_ne_hotyat_zhit_vmeste[p])):
                teams.add((h + 1, p + 1, z))
print(len(teams))
