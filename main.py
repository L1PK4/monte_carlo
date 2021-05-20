from mc_method import calc1, calc2
from numpy import sin, cos, pi 

def get_func(msg):
	return eval(f"lambda x, y : {input(msg)}")
	
def main():
	f = get_func('Enter f(x, y) = ')
	n = int(input("Enter n: "))
	print(f"Solution  = {calc1(f, n)}\nSolution 2 = {calc2(f, n)}")

if __name__ == '__main__':
	main()
