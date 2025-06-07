import tkinter as tk 
from tkinter import ttk 

def show(): 
    limit = num.get() 
    number = spin1.get() 
    generate = {limit}*{number} 
#window
window = tk.Tk() 


window.geometry("200x300") 

spin1 = tk.Spinbox(window,from_=1, to = 100)
spin1.pack()

num = tk.IntVar(value=10)


radio1 = ttk.Radiobutton(window,text = "10",variable=num,value=10)  
radio2 = ttk.Radiobutton(window,text = "15",variable=num,value=15) 
radio3 = ttk.Radiobutton(window,text = "20",variable=num,value=20) 
radio4 = ttk.Radiobutton(window,text = "25",variable=num,value=25) 
radio5 = ttk.Radiobutton(window,text = "30",variable=num,value=30)   

btn1 = tk.Button(window,text="GENERATE",command=show) 
btn1.pack()


radio1.pack()
radio2.pack()
radio3.pack()
radio4.pack()
radio5.pack()


window.mainloop()
