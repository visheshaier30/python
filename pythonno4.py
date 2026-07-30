print("---------Monthly Expense-------------")
n=int(input("enter number of expense:"))

expenses=[]
total=0
for i in range (n):
    amount=float(input(f"enter expense{i+1}"))
    expenses.append(amount)
    total +=amount

while True:
    print("/n===============expenses tracker menu=============")
    print("1.show all expenses ")
    print("2.show total expenses")
    print("3.add new expenses")
    print("4.exit")

    choice=int(input("enter your choice:"))

    if choice==1:
        print("expense list")
        for i in range(len(expenses)):
           print(f"Expense{i+1}:{expenses[i]}")
    elif choice==2:
        print("total monthly expense=",total)
    elif choice==3:
        new_expense=float(input("enter new expense:"))
        expenses.append(new_expense)
        total+=new_expense
    elif choice==4:
        print("thank you for using the monthly expenses tracker")
        break
    else:
        print("invalid choice! please try again.")