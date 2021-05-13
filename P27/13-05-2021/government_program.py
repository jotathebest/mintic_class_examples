# Determine if a student can access a government subsidy to access to school education. There are 3 requirements:
# 1. Must be not more than 40km to the round of school
# 2. Have more than 2 brothers
# 3. Family income is lower than 1000 dollars.

distance_to_school = input("Insert the distance to the school: ")
distance_to_school = float(distance_to_school)

if distance_to_school <= 40:
    # It fits more than 40 km from school
    number_of_brothers = input("Insert the number of brothers: ")
    number_of_brothers = float(number_of_brothers)
    if number_of_brothers >= 2:
        # it is possible
        family_income = input("Insert how much is your family income: ")
        family_income = float(family_income)
        if family_income <= 1000:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
