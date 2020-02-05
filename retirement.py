def calculate_retirement(age, salary, percentage, goal):
	saved = 0
	years = 0
	while saved < goal:
		total = salary * (percentage / 100)
		bonus = total * .35
		saved += total + bonus
		years += 1

	return age + years