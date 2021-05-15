# n = input()  1 < n < 10
# print --> 1^2 to n^2

# while <condition>:
#     <algorithm>

n = input("Insert a number: ")
n = int(n)

if not n in range(1, 11):
    print("Error")
else:
    while n >= 1:
        print(n ** 2)
        n = n - 1
        # n -= 1

# For

name = "jose"
result = False
for value in ["jose", True, "garcia", "jose", "jose", 2.3]:
    if name == value:
        result = True
if result:
    print("el nombre esta")

[i for i in range(1, 10)]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
