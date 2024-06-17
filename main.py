from random import choice, randint, shuffle
from tkinter import *




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += (choice(numbers) for i in range(randint(2, 4)))
    password_list += (choice(symbols) for i in range(randint(2, 4)))
    shuffle(password_list)
    password = "".join(password_list)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50) 

logo_img = PhotoImage(file="image/logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", font=(12))
website_label.grid(column=0, row=1) 
email_label = Label(text="Email/Username:", font=(12))
email_label.grid(column=0, row=2)
password_label = Label(text="Password:", font=(12))
password_label.grid(column=0, row=3)

#Entries
website_input = Entry(width=32)
website_input.grid(column=1, row=1)
website_input.focus()
email_input = Entry(width=50)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "samueltefera772@gmail.com")
password_input = Entry(width=32, bg="white")
password_input.grid(column=1, row=3)

#Button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)