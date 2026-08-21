marks = float(input("Enter graduation score: "))
backlogs = int(input("Enter number of active backlogs: "))

if marks >= 70:
    if backlogs == 0:
        print("Eligible for Placement")
    else:
        print("Not Eligible: Active backlogs are present")
else:
    print("Not Eligible: Graduation score is below 70%")