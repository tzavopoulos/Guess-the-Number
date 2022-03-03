from tkinter import *
import random
from tkinter import messagebox

root = Tk()

root.title('Guess the Number')

root.geometry('320x295')
root.config(background='black')

num = 0
correct = PhotoImage(master=root, file="check.png")
downarrow = PhotoImage(master=root, file="βέ-ος-που-είχνουν-προς-τα-πάνω-και-μια-σκά-α-38211965 2.png")
uparrow = PhotoImage(master=root, file="βέ-ος-που-είχνουν-προς-τα-πάνω-και-μια-σκά-α-38211965.png")

var = IntVar()


R1 = Radiobutton(root, text="Easy (0 - 50)", variable=var, value=1)
R1.grid(column=0, row=1)

R2 = Radiobutton(root, text="Normal (0 - 100)", variable=var, value=2)
R2.grid(column=1, row=1)

R3 = Radiobutton(root, text="Hard (0 - 150)", variable=var, value=3)
R3.grid(column=2, row=1)

def subaru():
    global num
    global gtn
    global correct
    global uparrow
    global downarrow
    a = int(ans_e.get())

    if a > gtn:
        num += 1

        lbl.config(image=downarrow)
        lbl_try.config(text=num)
    elif a < gtn:
        num += 1

        lbl.config(image=uparrow)
        lbl_try.config(text=num)
    elif a == gtn:
        num += 1

        lbl.config(image=correct)
        lbl_try.config(text=num)
        lbl_rigth = Label(root, text='Correct', background='black', foreground='pink', font=('Arial 13 bold'))
        lbl_rigth.grid(column=0, row=7)
        messagebox.showinfo("showinfo", "Correct")
        root.destroy()


def randomize():
    global gtn
    global var
    if var.get() == 1:
        gtn = random.randint(1, 50)
        print(gtn)
    elif var.get() == 2:
        gtn = random.randint(1, 100)
        print(gtn)
    elif var.get() == 3:
        gtn = random.randint(1, 150)
        print(gtn)









zari = PhotoImage(master=root, file="dice_PNG49.png")

lbl = Label(root, image=zari)
lbl.grid(column=0, row=5)

lbl_guess = Label(root, text='Guess the Number', background='black', foreground='pink', font=('Arial 25 bold'))
lbl_guess.grid(column=0, row=0, columnspan=3)
lbl_text = Label(root, text='In this Game you will try to find a secret number', background='black',foreground='white', font=('Arial 10 bold'))
lbl_text.grid(column=0, row=2, columnspan=3)

lbl_text2 = Label(root, text=' that is randomly chosen every round.', background='black',foreground='white', font=('Arial 10 bold'))
lbl_text2.grid(column=0, row=3, columnspan=3)

lbl_text3 = Label(root, text=' Try to guess it with the least possible tries.', background='black',foreground='white', font=('Arial 10 bold'))
lbl_text3.grid(column=0, row=4, columnspan=3)


ans_e = Entry(root)
ans_e.grid(column=1, row=5)


btn_exit = Button(root, text='Exit', background='pink', foreground='indigo', font=('Arial 13 bold'), command=root.destroy)
btn_exit.grid(column=2, row=5)

btn_rant = Button(root, text='Randomize', background='pink', foreground='indigo', font=('Arial 13 bold'), command=randomize)
btn_rant.grid(column=2, row=6)

btn_sub = Button(root, text='Submit', background='pink', foreground='indigo', font=('Arial 13 bold'), command=subaru)
btn_sub.grid(column=1, row=6)

lbl_try = Label(root, text=num, background='black', foreground='white', font=('Arial 13 bold'))
lbl_try.grid(column=0, row=7)


root.mainloop()
