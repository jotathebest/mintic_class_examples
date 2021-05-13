# https://www.codechef.com/problems/HS08TEST

# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction 
# if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction 
# (including bank charges). For each successful withdrawal the bank charges 0.50 $US. 
# Calculate Pooja's account balance after an attempted transaction. 

# Input:
# 30 120.00

# Output:
# 89.50

# Input:
# 42 120.00

# Output:
# 120.00

# Input:
# 300 120.00

# Output:
# 120.00

withdraw = float(input("Insert the withdraw: "))
balance = float(input("Insert the account's balance: "))

if withdraw % 5 != 0:
    print("You should use numbers divided by 5")
elif balance > withdraw + 0.5:
    new_balance = balance - (withdraw + 0.5)
    print(f"Your new account balance is {new_balance}")
else:
    print(f"You do not have enough money, your account balance is {balance}")
