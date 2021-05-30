email = input("Insert your email")

number = email.find("@")

if number > 0:
    print("válido")
else:
    print("no valido", end="")


# my_str = "testtest.com"

# my_str.find("@")
# -1
