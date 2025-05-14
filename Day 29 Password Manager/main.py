from tkinter import *
from tkinter import messagebox as tmsg
from random import choice, shuffle, randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = [chr(x+65) for x in range(26)] + [chr(x+97) for x in range(26)]
    numbers = [chr(x+48) for x in range(10)]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    character_list = [choice(letters) for x in range(randint(8, 10))]
    number_list = [choice(numbers) for x in range(randint(2, 4))]
    symbol_list = [choice(symbols) for x in range(randint(2, 4))]

    password_list = character_list + number_list + symbol_list
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():

    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()

    new_data = {
        website : {
            "user" : user,
            "password" : password
        }
    }
    
    if (len(website)==0 or len(user)==0 or len(password)==0):
        tmsg.showinfo(title="Incomplete Fields", message="Some fields are left empty")
    else:
        is_ok = tmsg.askokcancel(title=f"{website} password!", message=f"Your info: \nwebsite: {website} \nuser: {user} \npassword: {password}")

        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except Exception:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
            
            # website_entry.delete(0, END)
            # password_entry.delete(0, END)


# -------------------------------- For Searching the entry ---------------------------------------- #
def find_password():

    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except Exception:
        tmsg.showinfo(title="Problem Occurred!", message="No data file found")
    else:
        website = website_entry.get()
        if website in data:
            user = data[website]["user"]
            password = data[website]["password"]
            password_value.set(password)
            tmsg.showinfo(title=website, message=f"gmail: {user} \npassword: {password}")
        else:
            tmsg.showinfo(title="Problem Occurred!", message=f"No data entry found for {website}")




# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

# Logo on top of application
canvas = Canvas(root, height=200, width=200)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

# Website Specifying widgets
website_label = Label(root, text="Website: ")
website_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

website_value = StringVar()
website_entry = Entry(root, textvariable=website_value, width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="w", padx=5, pady=5)

search_button = Button(root, text="Search", command=find_password, padx=15)
search_button.grid(row=1, column=2,padx=5, pady=5)

# Email/ Username specifying widgets
user_label = Label(root, text="Email/Username: ")
user_label.grid(row=2, column=0, sticky="e", padx=5, pady=5)

user_value = StringVar()
user_entry = Entry(root, textvariable=user_value, width=35)
user_entry.insert(END, "SampleEmail@gmail.com")     # Insert your own email here
user_entry.grid(row=2, column=1, columnspan=2, sticky="w",padx=5, pady=5)

# password specifying widgets
password_label = Label(root, text="Password: ")
password_label.grid(row=3, column=0, sticky="e",padx=5, pady=5)

password_value = StringVar()
password_entry = Entry(root, textvariable=password_value, width=21)
password_entry.grid(row=3, column=1, sticky="w",padx=5, pady=5)

generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2,padx=5, pady=5)

# Add button
add_button = Button(root, text="Add", width=36, command=add_data)
add_button.grid(row=4, column=1, columnspan=2,padx=5, pady=5)

root.mainloop()