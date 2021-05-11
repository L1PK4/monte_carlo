from random import uniform
def solve(func, a, b, n):
	ans = 0
	for i in range(n):
		ans += func(uniform(a, b))
	return (b - a) * ans / n