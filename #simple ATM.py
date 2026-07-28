# simple ATM
balance = 100000
while True:
    print("\n   ATM MENU   ")
    print("1.Check Balance")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Exit")

    choice = input("Enter yo choice (1-4):")
    if choice == "1":
        print("your Balance:", balance)
    elif choice == "2":
        amount = float(input("enter deposit amount:"))
        balance = balance + amount
        print("amount deposited successfully !")
        print("current balacnce :", balance)
    elif choice == "3":
        amount = float(input("enter withdraw amount:"))
        if amount <= balance:
            balance = balance - amount
            print("please collect your cash")
            print("current balance:", balance)
        else:
            print("insufficient balance")
    elif choice == "4":
        print("Thank you ! Visit Again")
        break
    else:
        print("Invalid choice  please try again")
