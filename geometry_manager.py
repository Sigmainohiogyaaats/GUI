import tkinter as tk
from tkinter import ttk


#how to create window 
window = tk.Tk() 

#resizing window 
window.geometry('500x600') 
window.title('Basic widgets') 
#using pack for pos 

#making label 
##label.pack()#no paramaters the default is horizontally it will be in the middle and vertically the items will be positioned one after the other.


#button widget 

"""button = ttk.Button(window,text = 'CLOSE BUTTON',command = window.destroy,width=60,cursor = 'hand2',padding=(10,20)) 
button.pack(side='bottom',expand = True,fill = 'none') 


entry_box = ttk.Entry(window,width = 50,foreground = 'blue',background = 'red',font = ('Georgia',11),justify='center') 
entry_box.pack()


#place geometry manager
#making label 
label = ttk.Label(window,text = 'This is a label...',foreground = 'magenta',background = 'black') 
label.place(x = 5, y = 20)#no paramaters the default is horizontally it will be in the middle and vertically the items will be positioned one after the other.


#button widget 

button = ttk.Button(window,text = 'CLOSE BUTTON',command = window.destroy,width=60,cursor = 'hand2',padding=(10,20)) 
button.place(x = 5, y = 50) 


entry_box = ttk.Entry(window,width = 50,foreground = 'blue',background = 'red',font = ('Georgia',11),justify='center') 
entry_box.place(x = 5, y = 200)"""

#making label 
label = ttk.Label(window,text = 'This is a label...',foreground = 'magenta',background = 'black') 
label.grid(row= 0,column = 0)#no paramaters the default is horizontally it will be in the middle and vertically the items will be positioned one after the other.


#button widget 

button = ttk.Button(window,text = 'CLOSE BUTTON',command = window.destroy,width=60,cursor = 'hand2',padding=(10,20)) 
button.grid(row = 1,column = 1) 


entry_box = ttk.Entry(window,width = 20,foreground = 'blue',background = 'red',font = ('Georgia',11),justify='center') 
entry_box.grid(row = 1,column = 0)
window.mainloop() 