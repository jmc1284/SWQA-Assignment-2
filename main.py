import bmi
import retirement

def print_menu():
	print("\n" + 30 * '-')
	print("	     MENU")
	print(30 * '-' + "\n")
	print("1. BMI")
	print("2. Retirement Age")
	print("3. Exit\n")

	while True:
		try:
			choice = int(input("Enter your choice [1-3]: "))
			if choice in range(1,4):
				break
			else:
				print("That is not a valid choice please try again.\n")
		except ValueError:
			print("That is not a valid choice please try again.\n")	

	return choice


if __name__ == "__main__":
	choice = print_menu()
	while choice != 3:
		if choice == 1:
			print("\n" + 30 * '-')
			print("	     BMI")
			print(30 * '-' + "\n")
			print("Enter your height in feet then inches.\n")
			while True:
				try:
					height_ft = int(input("Feet: "))
					break
				except ValueError:
					print("That is not a valid number please try again.\n")
			while True:
				try:
					height_in = int(input("Inches: "))
					break
				except ValueError:
					print("That is not a valid number please try again.\n")
			while True:
				try:
					weight = int(input("\nEnter your weight in pounds: "))
					break
				except ValueError:
					print("That is not a valid number please try again.")

			bmi_value = bmi.calculate_bmi(height_ft, height_in, weight)
			category = bmi.get_category(bmi_value)

			print("\nBMI: " + str(bmi_value) + "\n" + "Category: " + category)

		if choice == 2:
			print("\n" + 30 * '-')
			print("	  Retirement")
			print(30 * '-' + "\n")
			
			while True:
				try:
					age = int(input("Enter your age: "))
					break
				except ValueError:
					print("That is not a valid number please try again.\n")
			while True:
				try:
					salary = int(input("Enter your annual salary: "))
					break
				except ValueError:
					print("That is not a valid number please try again.\n")
			while True:
				try:
					percentage = int(input("Enter the percentage saved annualy: "))
					break
				except ValueError:
					print("That is not a valid number please try again.\n")
			while True:
				try:
					goal = int(input("Enter desired retirement savings: "))
					break
				except ValueError:
					print("That is not a valid number please try again.\n")
			
			retirement_age = retirement.calculate_retirement(age, salary, percentage, goal)

			if retirement_age > 100: 
				print("\nYou will die before you reach your retirement.")
			else:
				print("\nYou will reach retirement at age " + str(retirement_age))

		choice = print_menu()
