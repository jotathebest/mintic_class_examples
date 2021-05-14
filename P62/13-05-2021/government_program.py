# Determine if a student can access a government subsidy to access to school education. There are 3 requirements:
# 1. Must live at less than 40km to the round of school
# 2. Have more than 2 brothers
# 3. Family income is lower than 1000 dollars.

distance_to_school = float(input("Insert the distance to the school: "))
num_brothers_and_sisters = int(input("How many brothers and sisters do you have?: "))
family_income = float(input("Insert your family income"))

if distance_to_school > 40:
    print("No")
elif num_brothers_and_sisters < 2:
    print("No")
elif family_income > 1000:
    print("No")
else:
    print("Yes")

# Operadores

# "es divisible" if num % 5 == 0 else "no es divisible"
