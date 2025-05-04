import tkinter as tk   
from tkinter import ttk
window = tk.Tk() 
window.geometry('500x400') 
window.title('spinbox and combobox') 

spinbox1 = tk.Spinbox(window,values = ['apple','banana','durian']) 
spinbox1.pack() 
spinbox2 = tk.Spinbox(window,from_=1, to = 200,increment=3) 
spinbox2.pack() 
spinbox2 = tk.Spinbox(window,from_=1, to = 200,increment=200,state='readonly') 
spinbox2.pack()  

combobox1 = ttk.Combobox(window,values = ['Biriyani','uttapam'],state = 'readonly')
combobox1.pack() 


















window.mainloop() 
