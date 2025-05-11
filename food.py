import tkinter as tk
from tkinter import ttk

# Create main window
root = tk.Tk()
root.title("Food Order")
root.geometry("400x400")
root.config(bg="lightblue")

# Menu Bar 
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)

#  Labels and Entries 
tk.Label(root, text="Email:", bg="lightblue").pack(pady=2)
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password:", bg="lightblue").pack(pady=2)
password_entry = tk.Entry(root, show="*")
password_entry.pack()

#  Food Selection 
tk.Label(root, text="Select Food:", bg="lightblue").pack(pady=2)
food_spin = tk.Spinbox(root, values=("Chicken sandwich", "B.L.T", "Veg sandwich", "None"))
food_spin.pack()

# Beverage Selection
tk.Label(root, text="Select Beverage:", bg="lightblue").pack(pady=2)
bev_spin = tk.Spinbox(root, values=("Cola", "Fanta", "Orange Juice", "Water", "None"))
bev_spin.pack()

# Dessert Selection
tk.Label(root, text="Select Dessert:", bg="lightblue").pack(pady=2)
dessert_spin = tk.Spinbox(root, values=("Ice Cream", "Ice Lolly", "Chocolate Cake", "None"))
dessert_spin.pack()

#  Progress Bar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)

def submit_order():
    progress["value"] = 100  
    root.update_idletasks()

submit_butn = tk.Button(root, text="Submit Order", command=submit_order)
submit_butn.pack(pady=10)


root.mainloop()
