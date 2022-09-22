N, L = map(int,input().split())
K = int(input())
A = list(map(int, input().split()))
A.append(L)

def check(len, L, A, K):
	cut_time = 0
	current_cut = 0
	for i in A:
		if cut_time == K + 1:
			return True
		if i - current_cut < len:
			continue
		else:
			current_cut = i
			cut_time += 1
	if current_cut != L or cut_time != K + 1:
		return False
	else:
		return True

def binary_search(L,K,A):
	Min = 0
	Max = L//(K+1)
	Try_v = (Min + Max) // 2

	while(Min != Max):
		if check(Try_v, L, A, K):
			Min = Try_v
			Try_v = (Max + Min) // 2 + 1
		else:
			Max = Try_v - 1
			Try_v = (Max + Min) // 2
	return (Min)

print(binary_search(L,K,A))