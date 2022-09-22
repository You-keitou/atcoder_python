N = int(input())
limit = N // 2

def check(res):
	if res[0] != "(":
		return False
	count = 1
	for c in res[1:]:
		if count < 0:
			return False
		if c == "(":
			count += 1
		else:
			count -= 1
	if not count:
		return True

if N % 2:
	pass
else:
	end = 0
	for i in range(limit,N):
		end += 2**i
	begin = 0
	for i in range(limit):
		begin += 2**i
	for i in range(begin, end+1):
		b = 2**(N-1)
		res = ""
		for _ in range(N):
			if i & b:
				res += ")"
			else:
				res += "("
			b >>= 1
		if check(res):
			print(res)
		