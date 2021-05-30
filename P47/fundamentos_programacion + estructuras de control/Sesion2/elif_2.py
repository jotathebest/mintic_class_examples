# genders --> M , F
gender = input("Insert your gender (F / M): ")
gender = gender.upper()

# if gender == "M":
#     print("valido")
# elif gender == "F":
#     print("valido")
# else:
#     print("inválido")

# gender = M
#  M != M or M != F
#  False or True
# if gender != "M" and gender != "F":
#     print("inválido")
# else:
#     print("válido")

# gender = M
#  M == M or M == F
#  True or False
if gender == "M" or gender == "F":
    print("válido")
else:
    print("inválido")
