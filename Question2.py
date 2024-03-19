def factorial(n):
    r = 1
    for i in range(n, 1, -1):
        r *= i
    return r
def printout(n):
    for j in range(n, 0, -1):
        result = factorial(j)
        print(result, end="")
        for i in range(j, 0, -1):
            print(f" {i}", end="")
        print("")

num = input("Input a number: ")

try:
    num = int(num)
except:
    print("Please use numbers, not words")
    exit()

printout(num)