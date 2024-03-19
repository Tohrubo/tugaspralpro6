def primechk(n):
    if n < 2:
        return False
    for i in range(2, round(n**(1/2))+1):
        if n % i == 0:
            return False
    return True
def primebelow(n):
    if n <= 2:
        print("No prime below 2")
        return None
    
    for i in range(n, 1, -1):
        if primechk(i):
            return i
        

num = input("Input a number: ")
try:
    num = int(num)
except:
    print("Please use numbers, not words")
    exit()
prime = primebelow(num)
print(f"Prime below {num} is {prime}")