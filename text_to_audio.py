import tkinter as tk 
import pyttsx3
 
# initializing pyttsx3 

engine = pyttsx3.init() 

def convert(): 
    selection = text.get("1.0", tk.END)  
    engine.say(selection)
    engine.runAndWait()


# main window 
window = tk.Tk() 
window.title("Text to audio") 
window.geometry("600x400") 

text = tk.Text(window, width= 50, height= 7, bg= "black", fg= "white") 
text.place(x = 90, y = 70) 

audio_btn = tk.Button(window, text = "Conversion_btn",command= convert ) 
audio_btn.place(x = 250, y = 200) 

window.mainloop()