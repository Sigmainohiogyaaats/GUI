import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import * 

library = {}

# FUNCTIONS
def on_select(event):
    #Show details of selected book
    selected_index = listbox.curselection()
    if selected_index:
        book_title = listbox.get(selected_index)
        details = library[book_title]
        show_detail = f"\nTitle   :   {book_title}\n"
        show_detail += f"Author  :   {details[0]}\n"
        show_detail += f"Year    :   {details[1]}\n"
        show_detail += f"Genre   :   {details[2]}"
        messagebox.showinfo("Book Details", show_detail)

def add_book():
    #Add a book to library
    title = entry_title.get()
    author = entry_author.get()
    year = entry_year.get()
    genre = entry_genre.get()
    if title and author and year and genre:
        library[title] = [author, year, genre]
        if title not in listbox.get(0, tk.END):
            listbox.insert(tk.END, title)
        clear_all()
    else:
        messagebox.showwarning("Warning", "All fields are mandatory!")

def clear_all():
    entry_title.delete(0, tk.END)
    entry_author.delete(0, tk.END)
    entry_year.delete(0, tk.END)
    entry_genre.delete(0, tk.END)

def reset():
    clear_all()
    listbox.delete(0, tk.END)
    library.clear()

def delete_book():
    #Delete selected book
    selected_index = listbox.curselection()
    if selected_index:
        book_title = listbox.get(selected_index)
        listbox.delete(selected_index) 
        del library[book_title]
    else:
        messagebox.showwarning("Warning", "Please select a book to delete.")

def open_file():
    #Open library data from file
    global library
    file_to_open = askopenfile()
    if file_to_open:
        reset()
        library = eval(file_to_open.read())
        for key in library:
            listbox.insert(tk.END, key)
    else:
        messagebox.showwarning("Warning", "Invalid file selected!")

def save_books():
    #Save library data into file
    file_to_save = asksaveasfile(defaultextension='.txt')
    if file_to_save:
        print(library, file=file_to_save)

#  MAIN WINDOW 
window = tk.Tk()
window.title("Book Library")
window.geometry("600x400")

# Listbox
listbox = tk.Listbox(window, width=30, height=15)
listbox.place(x=20, y=40)
listbox.bind('<<ListboxSelect>>', on_select)

# Buttons under listbox
delete_btn = tk.Button(window, text="Delete", command=delete_book)
delete_btn.place(x=20, y=320, width=80)

open_btn = tk.Button(window, text="Open", command=open_file)
open_btn.place(x=450, y=10, width=80)

# Labels and entries
tk.Label(window, text="Title:").place(x=300, y=50)
entry_title = tk.Entry(window, width=30)
entry_title.place(x=370, y=50)

tk.Label(window, text="Author:").place(x=300, y=80)
entry_author = tk.Entry(window, width=30)
entry_author.place(x=370, y=80)

tk.Label(window, text="Year:").place(x=300, y=110)
entry_year = tk.Entry(window, width=30)
entry_year.place(x=370, y=110)

tk.Label(window, text="Genre:").place(x=300, y=140)
entry_genre = tk.Entry(window, width=30)
entry_genre.place(x=370, y=140)

# Add button
add_btn = tk.Button(window, text="Add Book", command=add_book)
add_btn.place(x=450, y=200, width=100)

# Save button
save_btn = tk.Button(window, text="Save", command=save_books)
save_btn.place(x=300, y=350, width=300)

window.mainloop()
