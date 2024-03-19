# n = 0
# m = 2
# if n == 1:
#     if m == 2:
#         print("Yes")
#     else:
#         print("No")
# else:
#     if m != 4:
#         print("Absolutely No")
#     else:
#         print("Maybe Yes")

# for i in range(0, 100):
#     if i == 10:
#         continue
#     elif i == 20:
#         break
#     print(i, end=" ")

for i in range(10):
    for j in range(i):
        print(i, end=" ")
    print("")