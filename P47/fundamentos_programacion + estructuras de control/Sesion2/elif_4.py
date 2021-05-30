# gender --> M , F, if gender is not 'M' or 'F', print inválido
# email --> it must have the char '@', if it does not, print "invalido"
# probe that both gender and email are not empty, if they are, print "invalido"

gender = input("Insert your gender: ")
email = input("Insert your email: ")

gender = gender.upper()

# M
# M != F or M != M
# True and False
if gender != "F" and gender != "M":
    print("invalido")
elif email.find("@") == -1:
    print("invalido")
elif email == "" or gender == "":
    print("invalido")
else:
    print("valido")

if email != "" and gender != "":
    if email.find("@") >= 0 and gender == "F" and gender == "M":
        print("valido")
    else:
        print("invalido")
else:
    print("invalido")
