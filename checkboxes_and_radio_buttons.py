import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox 

def showresult(): 
    #getting value from string var object 
    selected_colour = colour.get() 
    message = f'Your selected colour is {selected_colour}'
    messagebox.showinfo('COLOUR',message)
window = tk.Tk() 
#creating string var/(creation of objectenabling it to bind all the different widgets)
colour = tk.StringVar(value = 'Red')
#radiobuttons 

red = ttk.Radiobutton(window,text = 'Red',variable=colour,value='Red')
blue = ttk.Radiobutton(window,text = 'Blue',variable=colour,value='Blue')
green = ttk.Radiobutton(window,text = 'Green',variable=colour,value='Green') 

red.pack() 
blue.pack()
green.pack()

generate = tk.Button(window,text='Generate',command=showresult) 
generate.pack()
window.mainloop()