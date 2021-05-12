n = input("Insert a number: ")
n = int(n)

is_odd = n % 2 != 0

if is_odd:
    print("Weird")
elif not is_odd and n >= 2 and n <= 5:
    print("Not Weird")
elif not is_odd and n >= 6 and n <= 20:
    print("Weird")
elif not is_odd and n > 20:
    print("Not Weird")
else:
    print("Not valid")
