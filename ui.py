from tkinter import *
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("Dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

# Initializing lists
cart = []
money = [0]

# Getting the screen size so the code would work with different devices.
def get_screen_size():
    width, height = app.winfo_screenwidth(), app.winfo_screenheight()
    print(f'{width}x{height}')
    return f'{width}x{height}'


app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry(get_screen_size())


# Bro is literally a bozo

# Making the function of the button
def add_item(name, price):
    x = ""
    money[0] = (int(str(money[0])) + price)
    cart.append(name)
    for item in set(cart):
        x += f'{item}      {cart.count(item)}'
        x += "\n"
    orders.configure(text=x + str(money[0]))
    #print(int(money[0]))

# Making the function of the button
# def burger_function():
#     x = ""
#     money[0] = (int(str(money[0])) + 10)
#     cart.append("Burger")
#     for item in set(cart):
#         x += f'{item}      {cart.count(item)}'
#         x += "\n"
#     #print(x)
#     orders.configure(text=x + str(money[0]))
    #print(int(money[0]))

# Making the images all of the same size to add them to the button
def resizing_function(path):
    img = Image.open(path)
    img = img.resize((200, 200))
    return img


# Making the exit button the menu the pops up when pressing on it
def exit_function():
    w=customtkinter.CTk()
    w.geometry("375x200")
    def yes():
        w.destroy()
        app.destroy()
    def no():
        w.destroy()
    label = customtkinter.CTkLabel(w, text="Do you really want to EXIT the app?", fg_color="transparent", font=("Serif fonts", 20))
    label.place(x=30, y=30)
    yes = customtkinter.CTkButton(w, text="Yes", fg_color="Red", command=yes)
    no = customtkinter.CTkButton(w, text="No", fg_color="Blue", command=no)
    yes.place(x=30, y=90)
    no.place(x=180, y=90)
    w.mainloop()


#Defining the image
twister_img = ImageTk.PhotoImage(resizing_function("twister.jpg"))
burger_img = ImageTk.PhotoImage(resizing_function("burger.png"))


# Making the UI
title = customtkinter.CTkLabel(app, text="Order", fg_color="transparent", font=("Serif fonts", 30), width=200, height=10)
title.place(x = 900, y=0)
title2 = customtkinter.CTkLabel(app, text="Order", fg_color="transparent", font=("Serif fonts", 30), width=200, height=10)
title2.place(x = 1450, y=0)
orders = customtkinter.CTkLabel(app, text="", fg_color="transparent", font=("Serif fonts", 30))
orders.place(x =1500, y=30)
                                
# Making the buttons
button = customtkinter.CTkButton(master=app, text="9 Dhs", command=lambda:add_item("Twister", 9), image=twister_img, compound="top")
button.place(x=120, y=130, anchor=customtkinter.CENTER)
button = customtkinter.CTkButton(master=app, text="10 Dhs", command=lambda:add_item("Burger", 10), image=burger_img, compound="top")
button.place(x=350, y=130, anchor=customtkinter.CENTER)

exit_btn = customtkinter.CTkButton(master=app, text="Exit", fg_color="Red", hover_color="#ff7377", command=exit_function)
exit_btn.place(x=1750, y=950)


# Running the main loop
app.mainloop()

# Checking what the user bought for debugging purposes
print("Item        QTY")
for item in set(cart):
    print(f'{item}      {cart.count(item)}')