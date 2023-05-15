import json
import datetime
import random


user_file = "user.json"
user_dairy = "diary.json"
quotes = "quotes.json"


def start_page():
    # Read Json file
    with open(user_file, "r") as file:
        data = json.load(file)

    registr_or_login = input("Welcom to My Way!!! Do you have account? ( yes / no ): ")
    if registr_or_login == "yes":
        user_email = input("Your Email please: ")
        user_pass = input("Your Pass: ")
        # Check if the user exists in the JSON data
        for d in data:
            if user_email == d["email"] and user_pass == d["ps"]:
                # print(f"Hallo {d['name']}")
                return d
        print("User not found")
        return None
    elif registr_or_login == "no":
        # Create new user
        new_user = {
            "name": input("Name: "),
            "email": input("Email: "),
            "ps": input("Password: "),
            "age": int(input("Age: ")),
            "hobby": input("Hobby: "),
            "diary": user_dairy
        }
        # Add the new user to the JSON data
        data.append(new_user)
        # Write the updated JSON data back to the file
        with open(user_file, "w") as file:
            json.dump(data, file)
        return new_user


user = start_page()
if user:
    print(f"Welcome back, {user['name']}!")
else:
    print("Please register a new account.")

menu = ["Life Rules"]
plan = ["Daily plan", "Year plan", "5 years plan", "10 years plan", "life goals"]
life_goals = ["Pesonal goals", "Career goals", "Business goals", "Financial goals", "Learning goals", "Fitness goals"]
for p in plan:
    print(p)
user_goals = {
    "time": input(f"With which do you like to start? :"),

}

date = datetime.datetime.now()
formatted_date = date.strftime("%d-%B-%Y")
new_day = {
    "date": formatted_date,
    "pages": input(f"{user['name']} How was your day?")
}
with open(user_dairy, "r") as date_file:
    diary = json.load(date_file)

for i in diary:
    for x in i:
     print(i[x])

diary.append(new_day)

with open(user_dairy, "w") as date_file:
    json.dump(diary, date_file)


with open(quotes, "r") as quotes_file:
    quotes_data = json.load(quotes_file)


show_quotes = random.choice(quotes_data)
finall_show_quotes = show_quotes["qoute"] + "\n" + show_quotes["Author"].rjust(60)
print(finall_show_quotes)
