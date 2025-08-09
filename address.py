import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import * 

address_book = {}


def on_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_value = listbox.get(selected_index)
        messagebox.showinfo("Selected Item", f"You selected: {selected_value}")

def add_item():
    new_name = entry_name.get()
    new_birthday = entry_birthday.get() 
    new_address = entry_address.get() 
    new_mobile = entry_mobile.get() 
    new_email = entry_email.get()
    if new_name and new_birthday and new_address and new_email and new_mobile: 
        address_book[new_name] = [new_birthday,new_address,new_mobile,new_email]
        

    else:
        messagebox.showwarning("Warning", "all fields are mandatory!") 
    
    for items in address_book:  
        listbox.insert(tk.END, items) 





def delete_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select an item to delete.") 

def open_file(): 
    file_to_open = askopenfile()
    if file_to_open:
        listbox.delete(0, tk.END)
        for item in file_to_open:
            listbox.insert(tk.END)

def save_items():
    file_to_save = asksaveasfile(defaultextension='.txt')
    if file_to_save:
        lb_items = listbox.get(0, tk.END)
        for item in lb_items:
            print(item, file=file_to_save)
        listbox.delete(0, tk.END)

#  MAIN WINDOW 
window = tk.Tk()
window.title("Address Book")
window.geometry("600x400")

# Listbox
listbox = tk.Listbox(window, width=30, height=15)
listbox.place(x=20, y=40)
listbox.bind('<<ListboxSelect>>', on_select)

# Buttons under listbox
edit_btn = tk.Button(window, text="Edit", command=on_select)
edit_btn.place(x=20, y=320, width=80)

delete_btn = tk.Button(window, text="Delete", command=delete_item)
delete_btn.place(x=110, y=320, width=80)

# Open button
open_btn = tk.Button(window, text="Open", command=open_file)
open_btn.place(x=450, y=10, width=80)

# Labels & entry fields 
name_label = tk.Label(window, text="Name:")
name_label.place(x=300, y=50)
entry_name = tk.Entry(window, width=30)
entry_name.place(x=370, y=50)

address_label = tk.Label(window, text="Address:")
address_label.place(x=300, y=80)
entry_address = tk.Entry(window, width=30)
entry_address.place(x=370, y=80)

mobile_label = tk.Label(window, text="Mobile:")
mobile_label.place(x=300, y=110)
entry_mobile = tk.Entry(window, width=30)
entry_mobile.place(x=370, y=110)

email_label = tk.Label(window, text="Email:")
email_label.place(x=300, y=140)
entry_email = tk.Entry(window, width=30)
entry_email.place(x=370, y=140)

birthday_label = tk.Label(window, text="Birthday:")
birthday_label.place(x=300, y=170)
entry_birthday = tk.Entry(window, width=30)
entry_birthday.place(x=370, y=170)

# Update/Add button
update_btn = tk.Button(window, text="Update/Add", command=add_item)
update_btn.place(x=450, y=200, width=100)

# Save button
save_btn = tk.Button(window, text="Save", command=save_items)
save_btn.place(x=300, y=350, width=300)


for i in range(1, 6):
    listbox.insert(tk.END)

window.mainloop()
