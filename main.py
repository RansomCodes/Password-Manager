from tkinter import *
from tkinter import messagebox
from random import randint, shuffle,choice
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols=[choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[choice(numbers) for _ in range(nr_numbers)]

    password_list=password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    for char in password_list:
        password+= char
    pass_entry.insert(0,password)
    pyperclip.copy(password)
  
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=web_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website)==0 or len(email)==0:
        messagebox.showerror(title="Oops",message="Please don't leave any of the fields empty") 
        return
    is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\n Is it ok to save?")
    if is_ok: 
        try:
            with open("data.json","r") as data_file:
                # json.dump(new_data,data_file,indent=4)
                data=json.load(data_file)
                data.update(new_data)
        except:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4) 
        finally:
            web_entry.delete(0,END)
            pass_entry.delete(0,END)
        
def search_password():
    website=web_entry.get()
    if len(website)==0:
        messagebox.showerror(title="Oops",message="Please Enter the File name")
        return
    try:
        with open("data.json","r") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Oops",message="No Data File Found")
    else:
        try:
            File_info=data[website]
        except KeyError:
            messagebox.showerror(title="Website",message="No details for the website exist")
        else:
            messagebox.showinfo(title=website,message=f"Email: {File_info['email']}\nPassword: {File_info['password']}")
        
    
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
pass_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pass_img)
canvas.grid(row=0,column=1)

web_label=Label(text="Website:")
web_label.grid(row=1,column=0)

email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)

pass_label=Label(text="Password:")
pass_label.grid(row=3,column=0)

#Entries 
web_entry=Entry(width=21)
web_entry.grid(row=1,column=1)
web_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"manmeet7210@gmail.com")
pass_entry=Entry(width=21) 
pass_entry.grid(row=3,column=1)

#Buttons
gen_pass_button=Button(text="Generate password",width=14,command=gen_pass)
gen_pass_button.grid(row=3,column=2)

add_button=Button(text="Add",width=25,command=save)   
add_button.grid(row=4,column=1,columnspan=2) 

search_button=Button(text="Search",width=13,command=search_password)
search_button.grid(row=1,column=2)





window.mainloop()