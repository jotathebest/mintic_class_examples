tax_factor = 0.0065
print("Enter the property lot number\nor type '0' to end: ", end="")
lot = int(input())

while lot != 0:
    value = float(input("Enter the property value: "))
    tax = value * tax_factor
    print(f"property tax: {round(tax, 3)}")
    print("Enter the property lot number\nor type '0' to end: ", end="")
    lot = int(input())
