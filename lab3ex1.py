age = int(input("Enter your age: "))
income = float(input("Enter annual family income: "))

if age < 25:
    if income < 300000:
        print("Eligible for Specialized Education Scholarship")
    else:
        print("Not Eligible: Income is ₹3,00,000 or above")
else:
    print("Not Eligible: Age must be below 25")