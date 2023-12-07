import tkinter as tk
from tkinter import Label, Entry, Button
from tkinter import PhotoImage

# setup
root = tk.Tk()
root.title("Epic Apple Co.")

# set window size to full screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

# background image
background_image = PhotoImage(file=r"C:\Users\Ellaine\Downloads\Epic Apple Co..png")
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

# fonts
label_font = ("Comic Sans MS", 20, "bold")
button_font = ("Comic Sans MS", 20, "bold")
result_font = ("Comic Sans MS", 20, "bold")

def calculate_max_apples(money, apple_price):
    # Calculate the maximum number of apples
    max_apples = money // apple_price

    # Calculate the remaining money
    remaining_money = money % apple_price

    return max_apples, remaining_money

def calculate_and_display():
    money = float(entry_money.get())
    apple_price = float(entry_price.get())

    max_apples, remaining_money = calculate_max_apples(money, apple_price)

    result_label.config(text=f"You can buy {max_apples} apples with {money:.2f} pesos and have {remaining_money:.2f} pesos remaining.")

# money frame
money_frame = tk.Frame(root)
money_frame.place(relx=0.5, rely=0.35, anchor="n")

# create and place labels, entry widgets, and button
label_money = Label(money_frame, text="Available Money: (in Peso/s)", font=label_font, fg="red")
label_money.pack()

entry_money = Entry(money_frame, width=50)  # Set width to 20 characters
entry_money.pack()

# price frame 
price_frame = tk.Frame(root)
price_frame.place(relx=0.5, rely=0.45, anchor="n")

label_price = Label(price_frame, text="Enter the Price of an Apple: (in Peso/s)", font=label_font, fg="red")
label_price.pack()

entry_price = Entry(price_frame, width=50)  # Set width to 20 characters
entry_price.pack()

calculate_button = Button(root, text="Calculate", command=calculate_and_display, font=button_font, fg="red")
calculate_button.place(relx=0.5, rely=0.55, anchor="n")

# result frame
result_frame = tk.Frame(root,bg="red")
result_frame.place(relx=0.5, rely=0.65, anchor="n")

result_label = Label(result_frame, text="", font=result_font, fg="red")
result_label.pack()

# start the main loop
root.mainloop()
