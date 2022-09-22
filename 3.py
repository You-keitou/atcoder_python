N = int(input())

def search_path(street, min_path, start, N):
	for i in range(start + 1, N):
		if street[start][i]:
			min_path[i] = min_path[start] + 1
			search_path(street, min_path, i, N)


min_path = [0 for _ in range(N)]

verticle = 0
max_path = 0
for i in range(N):
	if min_path[i] > max_path:
		verticle = i
		max_path = min_path[i]

min_path = [0 for _ in range(N)]

print(min_path)