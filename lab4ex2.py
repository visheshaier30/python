status = input("Enter atmospheric status: ").lower()

if status == "hot":
    print("Turn on AC.")
elif status == "cold":
    print("Activate heater.")
elif status == "normal":
    print("Climate is normal. Keep the system idle.")
else:
    print("Unknown atmospheric status.")