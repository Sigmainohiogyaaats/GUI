import tkinter as tk 
from tkinter import messagebox 


window = tk.Tk()
window.geometry("600x700")   

tk.Label(window,text = "FEEDBACK FORM",font = "Georgia").place(x=210, y = 30)

tk.Label(window,text="Give some feedback: ").place(x = 10,y = 50)

text = tk.Text(window, width=30, height = 7)
text.place(x=10, y=90)

tk.Label(window, text="Select your age:").place(x = 10, y = 250)


age_spinbox = tk.Spinbox(window, from_=18, to=60)
age_spinbox.place(x = 10, y = 300)

tk.Label(window, text="Rate the event").place(x = 10, y = 340)

rating = tk.StringVar(value="Excellent") 
tk.Radiobutton(window, text="Excellent", variable=rating, value="Excellent").place(x = 40,y = 370)
tk.Radiobutton(window, text="Good", variable=rating, value="Good").place(x = 40,y = 400)
tk.Radiobutton(window, text="Average", variable=rating, value="Average").place(x = 40,y = 430)
tk.Radiobutton(window, text="Poor", variable=rating, value="Poor").place(x = 40,y = 460) 
   
def submit():
    feedback_text = text.get()
    age = age_spinbox.get()
    rate = rating.get()
    result = f"Feedback: {feedback_text}\nSelected Age: {age}\nRating: {rate}"
    messagebox.showinfo("Submitted Information", result)

tk.Button(window, text="Submit", command=submit).place(x = 250,y = 500)

window.mainloop()