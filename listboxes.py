import tkinter as tk 
from tkinter import messagebox 

def on_select(event): 
    #getting the index of the item that has been clicked
    selected_index = my_items.curselection()
    #getting the value of selected index 
    selected_value = my_items.get(selected_index) 
    print(selected_value)
window = tk.Tk() 
#window.geometry("600x900") 

label = tk.Label(window,text = "Listbox",font="Ariel")  
label.pack()

items_to_add = ["Mango","apple", 1, 2, "True"]

my_items = tk.Listbox(window) 
my_items.pack()
for item in items_to_add: 
    my_items.insert(tk.END,item)

#Binding the selection events
my_items.bind('<<ListboxSelect>>',on_select)

submit = tk.Button(window,text = "submit")  
submit.pack() 

window.mainloop()

