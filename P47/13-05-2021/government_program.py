# Determine if a student can access a government subsidy to access to school education. There are 3 requirements:
# 1. Must not be farther than 40km to the round of school
# 2. Have more than 2 brothers
# 3. Family income is lower than 1000 dollars.

distance_to_school = input("Distance to School: ")

if distance_to_school < 40:
    # it is possible
    brothers_and_sisters =input("Insert how many brothers and sisters do you have?: ")
    if brothers_and_sisters > 2:
        # it is possible
        family_income = input("Insert your family's income: ")
        if family_income < 1000:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")

if distance_to_school > 40:
    print("No")
elif brothers_and_sisters < 2:
    print("No")
elif family_income > 1000:
    print("No")
else:
    print("Yes")
