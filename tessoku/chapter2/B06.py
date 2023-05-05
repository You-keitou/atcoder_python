N = int(input())
A = list(map(int, input().split()))

#あたりの累積和をとる
acc = [0]
for index, v in enumerate(A):
    if index == 0:
        acc.append(v)
    else:
        acc.append(v + acc[index])

print(acc)
Q = int(input())
query = [list(map(int, input().split())) for _ in range(Q)]

for q in query:
    l,r = q
    win = acc[r] - acc[l - 1]
    lose = r - l + 1 - win

    if win == lose:
        print("draw")
    elif win < lose:
        print("lose")
    else:
        print("win")