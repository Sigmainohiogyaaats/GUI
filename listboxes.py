import tkinter as tk 
from tkinter import messagebox 


def on_select(event): 
    #getting the index of the item that has been clicked
    selected_index = my_items.curselection()
    #getting the value of selected index 
    selected_value = my_items.get(selected_index) 
    print(selected_value) 

def list_add(): 
    value_store = entry_to_add.get()
    print(value_store) 
    my_items.insert(tk.END,value_store)

def list_delete(): 
    #getting the index number of the selected item that is supposed to be deleted 
    selected_index = my_items.curselection()#This will give a list as an answer. 
    for item in selected_index:
        my_items.delete(item)

    






window = tk.Tk() 
#window.geometry("600x900") 
tk.Label(text = 'Entry').pack()

entry_to_add = tk.Entry(window)
entry_to_add.pack()  

add = tk.Button(window,text = "ADD_item",command = list_add)
add.pack() 

delete = tk.Button(window,text = 'delete', command = list_delete) 
delete.pack()


label = tk.Label(window,text = "Listbox",font="Ariel")  
label.pack()

items_to_add = ["Mango","apple", 1, 2, "True"]

my_items = tk.Listbox(window) 
my_items.pack()
for item in items_to_add: 
    my_items.insert(tk.END,item) # insert has two parameters, First :position, Second :item to be added in the list. 
    #'Tk.END ' represents the 'End' of the list.

#Binding the selection events(for example a click)
my_items.bind('<<ListboxSelect>>',on_select)
#Bind is a function used to combine an action that you want to perform once any of the list item is clicked 
#"Listboxselect" is the clicking event. 
#'on_select' is the user defined function in which you can write down any action you want performed


window.mainloop()

