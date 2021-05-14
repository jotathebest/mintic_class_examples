# https://www.codechef.com/problems/HS08TEST

# Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the
# transaction if X is a multiple of 5, and Pooja's account balance has enough cash to
# perform the withdrawal transaction (including bank charges). For each successful
# withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an 
# attempted transaction.

# Input:
# 30 120.00

# Output:
# 89.50

# Example - Incorrect Withdrawal Amount (not multiple of 5)

# Input:
# 42 120.00

# Output:
# 120.00

# Example - Insufficient Funds

# Input:
# 300 120.00

# Output:
# 120.00

# "es divisible" if num % 5 == 0 else "no es divisible"

x = input("Insert the withdrawal: ")
balance = input("Insert the account's balance: ")

result = balance if not x % 5 == 0 or balance < x + 0.5 else balance - (x + 0.5)
print(result)
