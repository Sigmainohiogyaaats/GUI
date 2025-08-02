import tkinter as tk
from tkinter import messagebox 
from tkinter.filedialog import *



def on_select(event):
    #Show the selected item in a messagebox
    selected_index = listbox.curselection()
    if selected_index:
        selected_value = listbox.get(selected_index)
        messagebox.showinfo("Selected Item", f"You selected: {selected_value}")

def add_item():
    
    new_item = entry.get()
    if new_item:
        listbox.insert(tk.END, new_item)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter text to add.")

def delete_item():
    #Delete the selected item from the listbox
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)
    else:
        messagebox.showwarning("Warning", "Please select an item to delete.") 

def open_file(): 
    #open filedialog box to select the files you want to read and get the content 
    file_to_open = askopenfile() 

    if file_to_open: 
        listbox.delete(0,tk.END)

        #reading the content of the file 
        file_content = file_to_open.readlines()
        #file_content is a list that gets all the lines of the file. 
        for item in file_content: 
            listbox.insert(tk.END,item)

def save_items():
    
    """items = listbox.get(0, tk.END)
    if items:
        messagebox.showinfo("Save", f"Items saved: {', '.join(items)}") # comma and space used as delimitor for the different items, when shown in the message_box.
    else:
        messagebox.showwarning("Warning", "No items to save.")"""

    #saving listbox items onto a file.

    # getting the save-dialog box with the default extension txt. (txt file)  

    file_to_save = asksaveasfile(defaultextension= '.txt') 

    if file_to_save: 
        lb_items = listbox.get(0,tk.END) #lb_items is a list where you are going to get the data from the list box widget
        for item in lb_items:  
            print(item,file=file_to_save) 
        listbox.delete(0,tk.END)



                



# Main window
window = tk.Tk()
window.title("Memorizer")
window.configure(bg="#ffb6c1")  # Pink background
window.geometry("500x400")

# Save button
save_btn = tk.Button(window, text="SAVE", command=save_items)
save_btn.pack(pady=5)

# Entry for adding items
entry = tk.Entry(window)
entry.pack(pady=5)

# Add button
add_btn = tk.Button(window, text="ADD", command=add_item)
add_btn.pack(pady=5)





listbox = tk.Listbox(
    bg="red",
    fg="white",
    width=30,
    height=10
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


# Preload listbox with items
for item in range(1, 11):
    listbox.insert(tk.END, f"LIST {item}")

# Bind click event
listbox.bind('<<ListboxSelect>>', on_select) 

#Open button 
open_btn = tk.Button(window, text= "OPEN", command =open_file) 
open_btn.pack(side=tk.RIGHT, padx=5)

# Delete button
delete_btn = tk.Button(window, text="DELETE", command=delete_item)
delete_btn.pack(side=tk.LEFT, padx=5)

window.mainloop()
