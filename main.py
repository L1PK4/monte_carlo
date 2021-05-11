from monte_carlo import solve
def getf(text : str):
    return eval(f"lambda x : {input(text)}")


def main():
    f = getf("Enter f(x) = ")
    a, b, n = tuple(map(int, input("Enter a,b,n: ").split()))
    print(f"Integral = {solve(f, a, b, n)}")

if __name__ == "__main__":
    main()