print("===== DISCOUNT BILL =====")

amount = float(input("Enter total purchase amount: ₹"))
discount_percent = float(input("Enter discount percentage: "))

discount = amount * discount_percent / 100
final_amount = amount - discount

print("\n======= BILLING SUMMARY =======")
print(f"Purchase Amount : ₹{amount:.2f}")
print(f"Discount        : {discount_percent:.2f}%")
print(f"Discount Amount  : ₹{discount:.2f}")
print("--------------------------------")
print(f"Final Payable   : ₹{final_amount:.2f}")
print("================================")