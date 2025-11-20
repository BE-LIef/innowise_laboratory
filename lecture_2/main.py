def generate_profile(age):
    age = int(age)
    if 0<=age<=12:
        return "Child"
    elif 13<=age<=19:
        return "Teenager"
    elif age>=20:
        return "Adult"

user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)
current_age = int(2025 - birth_year)
list_hobbies = []

while True:
    user_hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if user_hobby.lower() == "stop":
        break
    list_hobbies.append(user_hobby)

life_stage = generate_profile(current_age)
user_profile = {'Name': user_name, 'Age': current_age, 'Life Stage': life_stage, 'Hobbies': list_hobbies}

print('-'*3)
print('Profile Summary:')
print('Name:', user_profile['Name'])
print('Age:', user_profile['Age'])
print('Life Stage:', user_profile['Life Stage'])

if not user_profile['Hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['Hobbies'])}):")
    for hobby in user_profile['Hobbies']:
        print(f"-{hobby}")

print('-'*3)