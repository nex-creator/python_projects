from tkinter import *
from tkinter import messagebox
from random import choice,shuffle,randint
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter = [choice(letters) for _ in range(randint(8,10))]
    password_symbol = [choice(symbols) for _ in range(randint(2,4))]
    password_number = [choice(numbers) for _ in range(randint(2,4))]
    password_list =  password_letter + password_symbol + password_number
    shuffle(password_list)
    print(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
# take entry into website then paswwrod
# when enter on add button it saves into text file
# Amazon | Angela@gmail.com | Password
def save():
    website = web_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email":email,
            "password":password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(message= "Please don't leave any empty field")
    else:
        try:
            with open("data.json", "r") as data_file:
                #reading the file
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            # File doesn't exist or is empty/invalid — start fresh
            data = {}
        data.update(new_data)
        with open("data.json", "w") as data_file:
                #saving the file
            json.dump(data, data_file, indent =4)
        web_entry.delete(0, END)
        password_entry.delete(0, END)
# ---------------------------- search password ------------------------------- #
def find_password():
    website = web_entry.get().lower()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title = "Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title = website, message = f"email: {email} \n"
                                              f"password: {password}")
        else:
            messagebox.showinfo(title ="Error", message="No details for the website exists")





# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50,pady =20)
canvas = Canvas(width = 200, height = 200)
image_logo =PhotoImage(file ="logo.png")
canvas.create_image(100,100, image = image_logo)
canvas.grid(row = 0, column=1)
# labels
website_label= Label(text ="Website:")
website_label.grid(row =1, column =0)
username_label= Label(text ="Email/Username:")
username_label.grid(row =2, column =0)
password_label= Label(text ="Password:")
password_label.grid(row =3, column =0)

#Entry
web_entry = Entry(width= 21)
web_entry.grid(row = 1, column = 1)
web_entry.focus()
username_entry = Entry(width= 42)
username_entry.grid(row = 2, column = 1, columnspan=2)
username_entry.insert(0,"angela@gmail.com")
password_entry=  Entry(width=21)
password_entry.grid(row= 3, column= 1)

#Button
generate_pass_button= Button(text= "Generate Paasword", command = generate_password)
generate_pass_button.grid(row =3, column = 2)
add_button = Button(text = "Add", width = 36, command = save)
add_button.grid(row =4, column = 1, columnspan =2)
search_button = Button(text = " Search",width = 20, command =  find_password)
search_button.grid(row= 1,column = 2)







window.mainloop()