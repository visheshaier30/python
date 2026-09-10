print("===== GROCERY BILL =====")

name1 = input("Enter item 1 name: ")
qty1 = int(input("Enter quantity: "))
price1 = float(input("Enter price per item: ₹"))

name2 = input("Enter item 2 name: ")
qty2 = int(input("Enter quantity: "))
price2 = float(input("Enter price per item: ₹"))

name3 = input("Enter item 3 name: ")
qty3 = int(input("Enter quantity: "))
price3 = float(input("Enter price per item: ₹"))

total1 = qty1 * price1
total2 = qty2 * price2
total3 = qty3 * price3

total = total1 + total2 + total3

print("\n========== FINAL BILL ==========")
print(f"{'Item':<15}{'Qty':<8}{'Price':<10}{'Amount':<10}")
print("--------------------------------------------")
print(f"{name1:<15}{qty1:<8}{price1:<10.2f}{total1:<10.2f}")
print(f"{name2:<15}{qty2:<8}{price2:<10.2f}{total2:<10.2f}")
print(f"{name3:<15}{qty3:<8}{price3:<10.2f}{total3:<10.2f}")
print("--------------------------------------------")
print(f"Total Bill: ₹{total:.2f}")