# ANSI escape codes for colors
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
RESET = "\033[1;37m"

# Display welcome banner
print(GREEN + "🖳 Welcome to the Tip Calculator 🖳 " + RESET)
print("=" * 50)

# Input section with colored prompts
bill = float(input(BLUE + "What was the total bill? $" + RESET))
tip = float(input(BLUE + "How much tip would you like to give? (Enter any number as percentage, e.g., 15 for 15%): " + RESET))
people = int(input(BLUE + "How many people to split the bill? " + RESET))

# Calculation of tip and final amounts
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Display results
print("\n" + "=" * 50)
print(RESET + "Calculation Results" )
print("-" * 50)
print(f"Bill: ${bill:.2f}")
print(f"Tip Percentage: {tip}%")
print(f"Total Tip: ${total_tip_amount:.2f}")
print(f"Total Bill (with tip): ${total_bill:.2f}")
print(f"Number of People: {people}")
print(f"Each Person Should Pay: ${final_amount:.2f}")
print("=" * 50)

input(RESET + "Press Enter to exit...")
