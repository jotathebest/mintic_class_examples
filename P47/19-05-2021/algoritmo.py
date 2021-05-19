keep_going = "y"
while keep_going == "y":
    sales = float(input("Enter the amount of sales: "))
    comm_rate = float(input("Enter the commission rate: "))
    commission = sales * comm_rate
    print("The commission is {:.2f}".format(commission))
    keep_going = input("Do you want to calculate another commision? Type 'y' for yes: ")
