def calculate_bmi(height_ft, height_in, weight):
	weight_conv = weight * .45
	height_conv = ((height_ft * 12) + height_in) * .025
	bmi = weight_conv / (height_conv ** 2)
	bmi = round(bmi, 2)

	return bmi

def get_category(bmi):
	if bmi < 18.5:
		category = "Underweight"
	if bmi >= 18.5 and bmi < 25:
		category = "Normal weight"
	if bmi >= 25 and bmi < 30:
		category = "Overweight"
	if bmi >= 30:
		category = "Obese"

	return category