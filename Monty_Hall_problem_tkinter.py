from tkinter import*
from tkinter.ttk import Combobox
from tkinter import messagebox
import random
import PIL
from PIL import ImageTk, Image

def choice():
    choice = combo.get()
    return choice

def get_opened_door():
    answ1 = list(filter(lambda x: x != car and x != int(choice()), doors))[0]
    return answ1

def get_closed_door():
    answ2 = list(filter(lambda x: x != int(choice()) and x != get_opened_door(), doors))[0]
    return answ2

def second_choice():
    lbgoat_image.configure(
        text=f'''Ok. But I want to open one door for you.
    Now I will open the door number {get_opened_door()}
    and we will see what's there. Oh! Goat here!
    Do you still want to open the door number {choice()}? '''
        )
    closed_doors = [get_closed_door(), int(choice())]
    closed_doors.sort()
    goat_image.pack()
    combo2['values'] = closed_doors
    combo2.pack()
    btn2 = Button(window, text="Send", bg="green", fg="white", command=clicked2)
    btn2.pack()
    lbl3.pack()

def clicked():
    a = combo.get()
    if a not in ("1", "2", "3"):
        messagebox.showerror('Error', 'Please take your choice')
    else:
        second_choice()

def clicked2():
    a = int(combo2.get())
    if a == car:
        lbl3.configure(text="Congratulation!")
        win_img.pack()

    else:
        lbl3.configure(text="Maybe next time")
        loss_img.pack()
 
window = Tk()
window.title("Monty Hall problem")
window.geometry('270x600')
first_image = PhotoImage(file='Monty.gif')
first_image = first_image.subsample(2)
Monty_img = Label(window, image=first_image)
Monty_img.pack()
second_image = PhotoImage(file='goat_2.gif')
second_image = second_image.subsample(2)
goat_image = Label(window, image=second_image)
third_img = PhotoImage(file='car.gif')
third_img = third_img.subsample(2)
win_img = Label(window, image=third_img)
last_img = PhotoImage(file='goat_3.gif')
last_img = last_img.subsample(2)
loss_img = Label(window, image=last_img)

doors = [1, 2, 3]
random.shuffle(doors)
car = random.randint(1, 3)

lbl = Label(window, text="Choose the door number(1,2 or 3):")
lbl.pack()
combo = Combobox(window)
combo['values'] = ("Your choice", 1, 2, 3)
combo.current(0)
combo.pack()
btn = Button(window, text="Send", bg="green", fg="white", command=clicked)
btn.pack()
lbgoat_image = Label(window)
lbgoat_image.pack()
lbl3 = Label(window)
combo2 = Combobox(window)
btn2 = Button(window)

window.mainloop()
