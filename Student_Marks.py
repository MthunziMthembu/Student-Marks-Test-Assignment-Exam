from tkinter import *
from tkinter import messagebox

root = Tk()

myLabel1 = Label(root,bg='red', text='Enter your test mark:')
myLabel1.grid(row=0, column=0)

myLabel2 = Label(root,bg='red', text='Enter your assignment mark:')
myLabel2.grid(row=1, column=0)

myLabel3 = Label(root, bg='red',text='Enter your examination mark:')
myLabel3.grid(row=2, column=0)

test_mark = Entry(root, fg='black', bg='gold',borderwidth=25)
test_mark.grid(row=0, column=1)

assignment_mark = Entry(root, fg='black',  bg='gold',borderwidth=25)
assignment_mark.grid(row=1, column=1)

examination_mark = Entry(root, fg='black', bg='gold',borderwidth=25)
examination_mark.grid(row=2, column=1)

def Student_marks():
    if test_mark.get() == "":
        messagebox.showerror("Error", "Please enter your test mark")
    elif not test_mark.get().isnumeric():
        messagebox.showerror("Data Type Error", "Please enter a number for test mark that is from 0 to 100.")
        test_mark.delete(0, END)
    elif not assignment_mark.get().isnumeric():
        messagebox.showerror("Data Type Error", "Please enter a number for assignment mark that is from 0 to 100.")
        assignment_mark.delete(0, END)
    elif not examination_mark.get().isnumeric():
        messagebox.showerror("Data Type Error", "Please enter a number for examination mark that is from 0 to 100.")
        examination_mark.delete(0, END)
    else:
        test = int(test_mark.get())
        assignment = int(assignment_mark.get())
        exam = int(examination_mark.get())

        if test >= 80 and test <= 100:
            messagebox.showinfo(message='You passed your test with a Distinction!')
        elif test > 50 and test < 80:
            messagebox.showinfo(message='You passed your test!')
        else:
            messagebox.showinfo(message='You failed your test.')

        if assignment >= 80 and assignment <= 100:
            messagebox.showinfo(message='You passed your assignment with a Distinction!')
        elif assignment > 50 and assignment < 80:
            messagebox.showinfo(message='You passed your assignment!')
        else:
            messagebox.showinfo(message='You failed your assignment. Try again.')

        if exam >= 80 and exam <= 100:
            messagebox.showinfo(message='You passed your examination with a Distinction!')
        elif exam > 50 and exam < 80:
            messagebox.showinfo(message='You passed your examination!')
        else:
            messagebox.showinfo(message='You failed your examination. Try again.')

myButton = Button(root, text='Submit', bg='gold',command=Student_marks)
myButton.grid(row=5, column=1)

root.mainloop()