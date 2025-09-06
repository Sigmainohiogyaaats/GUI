import tkinter as tk  
from tkinter import messagebox 

window = tk.Tk() 
window.title("tic tac toe") 
current_player = "X" 
buttons = [["", "", ""], ["", "", ""], ["", "", ""]]

def create_btns():  
    for r in range(0,3):  
        for c in range(0,3):  
            btn = tk.Button(window, text = "", bg= "black", width= 20, height= 8) 
            btn.grid(column= c,row= r) 
            buttons[r][c] = btn  

def check_winner(): 
    pass




def on_button_click(r, c):  
    global current_player 
    if buttons[r][c]["text"] == "":
        buttons[r][c]["text"] = current_player 













create_btns()

window.mainloop()