D = int(input())
N = int(input())

Sanka = [list(map(int, input().split())) for _ in range(N)]

Zenjituhi = [0] * (D + 1)

for v in Sanka:
    l, r = v
    Zenjituhi[l] += 1
    Zenjituhi[r + 1] -= 1

ans = []

for index, i in enumerate(Zenjituhi):
    if index == 0:
        ans.append(i)
    else:
        ans.append( i + ans[index - 1])

print(ans)