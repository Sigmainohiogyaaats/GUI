from tkinter import *

# Function to handle order submission
def submit_order():
    food_item = entry.get()
    label.config(text=f"Order: {food_item}")

# Create main window
root = Tk()
root.title("Food Delivery App")
root.geometry("300x200")  # Set window size 

# Create a label
label = Label(root, text="Welcome to Food Express!", font=("Arial", 12))
label.pack(pady=10)

# Create an entry box
entry = Entry(root, width=30, bd=2, bg="lightyellow", fg="black")
entry.pack(pady=5)
entry.insert(0, "Enter your food item")

# Create buttons
deliver_button = Button(root, text="Order Now", bg="green", fg="white", command=submit_order)
deliver_button.pack(pady=5)

exit_button = Button(root, text="Exit", bg="red", fg="white", command=root.quit)
exit_button.pack(pady=5)

# Run the main loop
root.mainloop()