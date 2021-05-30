# email --> it must have the char '@'

email = input("Insert your email: ")

if email.find("@") == -1:
    print("invalido")
else:
    print("valido")
