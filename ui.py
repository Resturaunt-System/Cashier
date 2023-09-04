import customtkinter as ctk
from PIL import Image
from json import load as json_load

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Initializing lists
cart = []
money = [0]

RESTURAUNT_DATA = json_load(open("data.json", "r"))

# Getting the screen size so the code would work with different devices.
def get_screen_size():
    width, height = app.winfo_screenwidth(), app.winfo_screenheight()
    print(f'{width}x{height}')
    return f'{width}x{height}'

# Making the images all of the same size to add them to the button
def resize_image(path, size):
    img = Image.open(path)
    img = img.resize(size)
    return img

# Making the exit button the menu the pops up when pressing on it
def exit():
    w=ctk.CTk()
    w.geometry("375x200")
    label = ctk.CTkLabel(w, text="Do you really want to EXIT the app?", fg_color="transparent", font=("Serif fonts", 20))
    label.place(x=30, y=30)
    yes = ctk.CTkButton(w, text="Yes", fg_color="Red", command=lambda: (w.destroy(), app.destroy())) # It is in tuples so it would run both commands
    no = ctk.CTkButton(w, text="No", fg_color="Blue", command=w.destroy)
    yes.place(x=30, y=90)
    no.place(x=180, y=90)
    w.mainloop()


app = ctk.CTk()  # create CTk window like you do with the Tk window
app.title("Resturaunt System")
app.geometry("1024x768")
app.minsize(1024, 768)

# Categories section takes 75%, selected item takes 12% and the current order takes 12%
app.columnconfigure(0, weight=75)
app.columnconfigure((1, 2), weight=12)

app.rowconfigure(1, weight=1)

title = ctk.CTkLabel(app, text=RESTURAUNT_DATA["name"], font=("Arial", 64))
title.grid(row=0, column=0, sticky="nsew", columnspan=3, padx=10, pady=10)

# CATEGORIES/ITEMS SECTION
items_outer = ctk.CTkFrame(app)
items_outer.rowconfigure(0, weight=100)
items_outer.rowconfigure(1, weight=1)
items_outer.columnconfigure(0, weight=1)

items = ctk.CTkScrollableFrame(items_outer)
items.columnconfigure((0,1), weight=1)
for i, category in enumerate(RESTURAUNT_DATA['categories']):
    category_name = category['name']
    category_button = ctk.CTkButton(items, text=category_name, width=200, height=200, font=("Arial", 32))
    category_button.grid(row=i // 2, column=i % 2, sticky="news", padx=5, pady=5)
    category_button.configure(width=200, height=200)

items.grid(row=0, column=0, sticky="nsew")

back = ctk.CTkButton(items_outer, text="Back", font=("Arial", 32), state="disabled")
back.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

items_outer.grid(row=1, column=0, sticky="nsew")

selected = ctk.CTkFrame(app)
selected.grid(row=1, column=1, sticky="nsew")

order = ctk.CTkFrame(app)
order.grid(row=1, column=2, sticky="nsew")

app.mainloop()

# Checking what the user bought for debugging purposes
print("Item        QTY")
for item in set(cart):
    print(f'{item}      {cart.count(item)}')