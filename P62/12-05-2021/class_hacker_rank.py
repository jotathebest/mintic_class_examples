n = int(input("Insert a number: "))

is_odd = n % 2 != 0
# is_even = n % 2 == 0

if is_odd:
    print("Weird")
else:
    if not is_odd and n >= 2 and n <= 5:
        print("Not Weird")
    if not is_odd and n in range(6, 21):
        print("Weird")
    if not is_odd and n > 20:
        print("Not Weird")
