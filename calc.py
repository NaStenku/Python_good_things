from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox

def clicked():
    a = combo.get()
    if a == "Your choice":
        messagebox.showerror('Error', 'Please take your choice')
    else:
        lbl2.configure(text="But first")

def error():
    messagebox.showerror('Error', 'Please take yor choice')

window = Tk()
window.title("Monty Hall problem")
window.geometry('600x400')

lbl = Label(window, text="Choose the door number(1,2 or 3):", font=("Arial Bold", 24))
lbl.grid(column=0, row=0)
btn = Button(window, text="Send", bg="green", fg="white",command=clicked)
btn.grid(column=0, row=2)
lbl2 = Label(window, font=("Arial Bold", 24))
lbl2.grid(column=0, row=3)
combo = Combobox(window)
combo['values'] = ("Your choice", 1, 2, 3)  
combo.current(0)
combo.grid(column=0, row=1) 



window.mainloop()
