def printout(x, y):
    count = 1
    for i in range(y):
        for j in range(x):
            print(count, end=" ")
            count += 1
        print("")

height = input("Input height: ")
width = input("Input width: ")

try:
    height = int(height)
    width = int(width)
except:
    print("Please use numbers, not words")
    exit()

printout(width, height)