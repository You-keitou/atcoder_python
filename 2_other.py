N = int(input())

if N % 2:
	exit()

flag1 = "("
flag2 = ")"

def rec(flag, count, N):
	if count < 0:
		return
	if not N:
		if not count:
			print(flag)
		return
	rec(flag + flag1, count + 1, N - 1)
	rec(flag + flag2, count - 1, N - 1)

rec("", 0, N)