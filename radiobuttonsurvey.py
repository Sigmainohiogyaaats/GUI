import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Multiple Choice Question")
window.geometry("600x900")  

# Create a label for the question
question_label = tk.Label(window, text="Q1: What should you do?", font=("Arial", 10))
question_label.place(x = 2,y=0)

# Variable to track selected radio button
selected_q1 = tk.StringVar(value="E")
selected_q2 = tk.StringVar(value="E")
selected_q3 = tk.StringVar(value="E")
selected_q4 = tk.StringVar(value="E")
selected_q5 = tk.StringVar(value="E")

# Create each radio button 
radio1 = tk.Radiobutton(window,text="A) Stay silent to avoid embarrassment",variable=selected_q1,value="A",font=("Arial", 9))
radio1.place(x = 15,y = 40)

radio2 = tk.Radiobutton(window,text="B) Give an honest update and explain the reason",variable=selected_q1,value="B",font=("Arial", 9))
radio2.place(x = 15,y = 60)

radio3 = tk.Radiobutton(window,text="C) Blame someone else on the team",variable=selected_q1,value="C",font=("Arial", 9))
radio3.place(x = 15,y = 80)

radio4 = tk.Radiobutton(window,text="D) Say it’s done, and fix it later",variable=selected_q1,value="D",font=("Arial", 9))
radio4.place(x = 15,y = 100)


question_label2 = tk.Label(window, text="Q2: How should you respond", font=("Arial", 10))
question_label2.place(x = 2,y = 140)   

radio5 = tk.Radiobutton(window,text="A) Publicly point out their mistake",variable=selected_q2,value="A",font=("Arial", 9))
radio5.place(x = 15,y = 160) 

radio6 = tk.Radiobutton(window,text="B) Privately inform them and help resolve it",variable=selected_q2,value="B",font=("Arial", 9))
radio6.place(x = 15,y = 180) 

radio7 = tk.Radiobutton(window,text="C) Roll back the code without telling anyone",variable=selected_q2,value="C",font=("Arial", 9))
radio7.place(x = 15,y = 200) 

radio8 = tk.Radiobutton(window,text="D) Wait for them to realize on their own",variable=selected_q2,value="D",font=("Arial", 9))
radio8.place(x = 15,y = 220) 



question_label3 = tk.Label(window, text="Q3: What do you do?", font=("Arial", 10))
question_label3.place(x = 2,y = 260)  



radio9 = tk.Radiobutton(window,text="A) Try it alone even if unsure",variable=selected_q3,value="A",font=("Arial", 9))
radio9.place(x = 15,y = 280) 

radio10= tk.Radiobutton(window,text="B) Ask a senior for help or guidance",variable=selected_q3,value="B",font=("Arial", 9))
radio10.place(x = 15,y = 300) 

radio11 = tk.Radiobutton(window,text="C) Decline the task entirely",variable=selected_q3,value="C",font=("Arial", 9))
radio11.place(x = 15,y = 320) 

radio12 = tk.Radiobutton(window,text="D) Postpone it for later",variable=selected_q3,value="D",font=("Arial", 9))
radio12.place(x = 15,y = 340) 



question_label4 = tk.Label(window, text="Q4: What's the most constructive way to respond?", font=("Arial", 10))
question_label4.place(x = 2,y = 360)  



radio13 = tk.Radiobutton(window,text="A) Join one side", variable=selected_q4,value="A",font=("Arial",9))
radio13.place(x = 15,y = 380) 

radio14= tk.Radiobutton(window,text="B) Try to calm both and suggest taking it offline", variable=selected_q4,value="B",font=("Arial", 9))
radio14.place(x = 15,y = 400) 

radio15 = tk.Radiobutton(window,text="C) Ignore the situation", variable=selected_q4,value="C",font=("Arial", 9))
radio15.place(x = 15,y = 420) 

radio16 = tk.Radiobutton(window,text="D) Leave the meeting", variable=selected_q4,value="D",font=("Arial", 9))
radio16.place(x = 15,y = 440) 



question_label5 = tk.Label(window, text="Q5: What action do you take?", font=("Arial", 10))
question_label5.place(x = 2,y = 480)  



radio17 = tk.Radiobutton(window,text="A) Skip testing and submit",variable=selected_q5,value="A",font=("Arial",9))
radio17.place(x = 15,y = 500) 

radio18= tk.Radiobutton(window,text="B) Write and run your own basic tests",variable=selected_q5,value="B",font=("Arial", 9))
radio18.place(x = 15,y = 520) 

radio19 = tk.Radiobutton(window,text="C) Delay submission without explanation",variable=selected_q5,value="C",font=("Arial", 9))
radio19.place(x = 15,y = 540) 

radio20 = tk.Radiobutton(window,text="D) Push it to production anyway",variable=selected_q5,value="D",font=("Arial", 9))
radio20.place(x = 15,y = 560) 

def show_results():
    result = (
        f"Your selected options:\n\n"
        f"Q1: {selected_q1.get()}\n"
        f"Q2: {selected_q2.get()}\n"
        f"Q3: {selected_q3.get()}\n"
        f"Q4: {selected_q4.get()}\n"
        f"Q5: {selected_q5.get()}\n"
    )
    messagebox.showinfo("Submitted Answers", result)

# Submit Button
submit_button = tk.Button(window, text="Submit", command=show_results, font=("Arial", 10), bg="lightblue")
submit_button.place(x = 15,y = 600) 


window.mainloop()