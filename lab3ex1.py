name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter annual family income: "))
caste = input("Enter your caste (SC/ST/OBC/General): ").upper()

if age < 25:
    if income < 300000:
        if caste in ["SC", "ST", "OBC","NT","VJT"]:
            print("Eligible for Specialized Education Scholarship")
            result="Eligible for Specialized Education Scholarship"
        else:
            print("Not Eligible: Caste is General")
            result="Not Eligible "
    else:
        print("Not Eligible: Income is 300000 or above")
else:
    print("Not Eligible: Age must be below 25")

print("====================== Display ===================")
print(" Name : ",name)
print(" Age : ",age)
print(" Income : ",income)
print(" Caste : ",caste)
print("Status",result)
