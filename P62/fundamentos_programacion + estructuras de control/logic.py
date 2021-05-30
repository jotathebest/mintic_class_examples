# AND
input_1 = True
input_2 = False
input_3 = True
print(input_1 and input_2 and input_3)

# OR

input_1 = False
input_2 = False
input_3 = True
input_4 = True
print(input_1 or input_2 or input_3)
print((input_1 and input_3) or (input_2 and input_4))
print(input_1 and input_3 or input_2 and input_4)

# NOT
print(not(input_1 and input_3 or input_2 and input_4))
