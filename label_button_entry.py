import tkinter as tk 

#how to create window 
window = tk.Tk() 

#resizing window 
window.geometry('500x700') 
window.title('Basic widgets') 

#making label 
label = tk.Label(window,text = 'This is a label...',fg = 'magenta',bg = 'white') 
label.pack()


#button widget 

button = tk.Button(window,text = 'CLOSE BUTTON',width = 40,height = 2,command = window.destroy) 
button.pack()

window.mainloop()  



