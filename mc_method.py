from random import uniform

def calc1(func, N):
	ans = 0
	for i in range(N):
		ans += func(uniform(0, 1), uniform(0, 1))
	return ans / N

def calc2(func, N):
	ans = 0
	for i in range(N):
		ans += (uniform(0, 1) < func(uniform(0, 1), uniform(0, 1)))
	return ans / N