
# Campus Store Checkout System
# Module 2: Operators and Expressions

print("=" * 50)
print("          CAMPUS STORE CHECKOUT SYSTEM")
print("=" * 50)

# Display available items
available_items = ["Pen", "Notebook", "Pencil", "Eraser"]

print("Available Items: Pen, Notebook, Pencil, Eraser")
print("=" * 50)

# Collect customer information
customer_name = input("Enter customer name: ")
selected_item = input("Enter selected item: ")
unit_price = float(input("Enter unit price (N): "))
quantity = int(input("Enter quantity: "))

student_response = input("Are you a student? (yes/no): ").lower()
amount_paid = float(input("Enter amount paid (N): "))

# Calculate subtotal
subtotal = unit_price * quantity

# Calculate 10% discount
discount = subtotal * 0.10
discounted_amount = subtotal - discount

# Calculate 5% service charge after discount
service_charge = discounted_amount * 0.05

# Calculate final total
final_total = discounted_amount + service_charge

# Calculate payment difference
payment_difference = amount_paid - final_total

# Demonstrate augmented assignment
points = 0
points += quantity

# Demonstrate membership operator
valid_item = selected_item.title() in available_items

# Demonstrate comparison operator
payment_sufficient = amount_paid >= final_total

# Demonstrate logical AND and parentheses
student_eligibility = (
    (subtotal >= 1000) and (student_response == "yes")
)

# Display customer receipt
print("\n")
print("=" * 50)
print("                CUSTOMER RECEIPT")
print("=" * 50)

print(f"Customer Name          : {customer_name}")
print(f"Selected Item          : {selected_item}")
print(f"Unit Price             : N{unit_price:,.2f}")
print(f"Quantity               : {quantity}")

print("-" * 50)

print(f"Subtotal               : N{subtotal:,.2f}")
print(f"Discount (10%)         : N{discount:,.2f}")
print(f"Discounted Amount      : N{discounted_amount:,.2f}")
print(f"Service Charge (5%)    : N{service_charge:,.2f}")
print(f"Final Total            : N{final_total:,.2f}")

print("-" * 50)

print(f"Amount Paid            : N{amount_paid:,.2f}")
print(f"Payment Difference     : N{payment_difference:,.2f}")
print(f"Payment Sufficient     : {payment_sufficient}")
print(f"Valid Item             : {valid_item}")
print(f"Student Eligible       : {student_eligibility}")
print(f"Points Earned          : {points}")

print("=" * 50)
print("Thank you for shopping at Campus Store!")
print("=" * 50)
