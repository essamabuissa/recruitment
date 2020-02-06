def main():
	skills = ["Python", "C++", "JavaScript", "Meeting", "Leeting", "Eating"]
	cv = {"name":"","age":0,"experience":0}
	print("Welcome to the special recruitment program, please answer the following questions:")
	cv['name'] = input("What\'s your name? ")
	cv['age']  = int(input("How old are you? "))
	cv['experience'] = int(input("How many years of experience do you have? "))
	cv['skills'] = []
	print()
	counter = 1
	for skill in skills:
		print(f"{counter}.{skill}")
		counter += 1
	print()
	choose_skill = int(input("Choose a skill from above by entering its number: "))
	cv['skills'].append(skills[choose_skill -1])
	choose_skill = int(input("Choose another skill from above by entering its number: "))
	cv['skills'].append(skills[choose_skill -1])
	if cv['age'] >= 25 and cv['age'] <= 40 and cv['experience'] > 5 and skills[5] in cv['skills']:
		print("Congrats you are accepted")
	else:
		print("Sorry you are rejected")


if __name__ == '__main__':
	main()
