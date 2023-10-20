pinacolada = list(map(int, input().split()))
n = int(pinacolada[0])
m = int(pinacolada[1])
members = [set([i+1]) for i in range(n)]
num = set([i+1 for i in range(n)])
for i in range(m):
 abuba = list(map(int, input().split()))
 members[int(abuba[0])-1].add(int(abuba[1]))
 members[int(abuba[1])-1].add(int(abuba[0]))

vars = set()
for i in range(n):
 for j in range(i+1, n):
  if(j+1 in members[i]):
   continue
  for k in (num - (members[i] | members[j])):
   vars.add(str(sorted([i+1, j+1, k])))

print(len(vars))