import customtkinter as ctk
from PIL import Image
from json import load as json_load
from time import sleep
import base64
import io
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

ctk.set_appearance_mode("system")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# Initializing lists
cart = []
money = [0]

RESTURAUNT_DATA = json_load(open("data.json", "r"))

# Getting the screen size so the code would work with different devices.
def get_screen_size():
    width, height = app.winfo_screenwidth(), app.winfo_screenheight()
    # print(f'{width}x{height}')
    return f'{width}x{height}'

# Deocde the ranch sauce for the program to execute without errors.
def decode_image(path):
    with open(path , "rb") as image_file :
        data = base64.b64encode(image_file.read())    
    with open(f"{path[:-4]}.txt", "wb") as new_file:
        # data = io.BytesIO(data.getbuffer())
        new_file.write(data)
    # return data.decode('utf-8')

# decode_image("assets/burger_beef.jpg")

def define_image(image_name, size):
    with open(f"{dir_path}/assets/{image_name}.txt", "rb") as image_file:
        decoded_string = base64.b64decode(image_file.read())
    _bytes = io.BytesIO(decoded_string)
    img = ctk.CTkImage(light_image=Image.open(_bytes), dark_image=Image.open(_bytes), size=size)
    return img



# Making the exit button the menu the pops up when pressing on it
def _exit():
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

category_items = ctk.CTkScrollableFrame(items_outer)
category_items.columnconfigure((0,2), weight=1)
# category_items.grid()
category_items.grid_forget()

orders = ctk.CTkFrame(app)
order = ctk.CTkScrollableFrame(orders)
order_label = ctk.CTkLabel(order)

def add_item(item_id, price):
    x = ""
    money[0] = (int(str(money[0])) + price)
    cart.append(item_id)
    for item in set(cart):
        x += f'{item}      {cart.count(item)}'
        x += "\n"
    order_label.configure(text=x + str(money[0]))
    print(x)

def replace_frame(current_frame, new_frame, **kwargs):
    row, column = 0, 0
    current_frame.grid_forget()
    new_frame.grid(row=row, column=column, sticky="nsew", **kwargs)
    return new_frame

for i, category in enumerate(RESTURAUNT_DATA['categories']):
    category_name = category['name']
    category_id = category['id']
    category_button = ctk.CTkButton(items, text=category_name, width=200, height=200, font=("Arial", 32), command=lambda category_id=category_id: open_category(category_id))
    category_button.grid(row=i // 2, column=i % 2, sticky="news", padx=5, pady=5)

# This funciton will be called when any of the categories buttons is pressed
def open_category(_id: str):
    replace_frame(items, category_items)
    for category in (RESTURAUNT_DATA["categories"]):
        if category['id'] == _id:
            print(category['items'])
            for i in range(len(category['items'])):
                item_name = category['items'][i]['name']
                item_id = category['items'][i]['id']
                item_price = int(category['items'][i]['price'])
                item = ctk.CTkButton(category_items, text=item_name, width=200, height=200, compound="top", image=define_image(item_id, (200, 200)), command=lambda: add_item(item_name, item_price))
                item.grid(row=i // 2, column = i % 2, sticky="news", padx=5, pady=5)
     

     
items.grid(row=0, column=0, sticky="nsew")


back = ctk.CTkButton(items_outer, text="Back", font=("Arial", 32), command=lambda: replace_frame(category_items, items))
back.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)


items_outer.grid(row=1, column=0, sticky="nsew")


selected = ctk.CTkFrame(app)
selected.grid(row=1, column=1, sticky="nsew")


orders.grid(row=1, column=2, sticky="nsew")


app.mainloop()

# Checking what the user bought for debugging purposes
print("Item        QTY")
for item in set(cart):
    print(f'{item}      {cart.count(item)}')
