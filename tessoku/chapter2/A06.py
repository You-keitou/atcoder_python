N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int,input().split())) for _ in range(Q)]

sum = [0]
for index, i in enumerate(A):
    if index == 0:
        sum.append(i)
    else:
        sum.append(i + sum[index])

for q in query:
    print(sum[q[1]] - sum[q[0]-1])

