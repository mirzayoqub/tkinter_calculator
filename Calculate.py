# Import Module
from tkinter import *
import tkinter as tk
import tkinter.messagebox

# create root window
root = Tk()

# root window title and dimension
root.title("Welcome to App")

# Set geometry(widthxheight)
root.geometry('500x300')
frame = tk.Frame(master=root, bg="grey", padx=10)
frame.pack()
# adding menu bar in root window
# new item in menu bar labelled as 'New'
# adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='Calculate', menu=item)
root.config(menu=menu)

# adding Entry Field
txt = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
txt.grid(row=0, column=1, columnspan=3, ipady=2, pady=2)


def answer():
    try:
        a = str(eval(txt.get()))
        txt.delete(0, tk.END)
        txt.insert(0, a)
    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")


# function to display user text when
# button is clicked
def myclick(number):
    txt.insert(tk.END, number)


def clear():
    txt.delete(0, tk.END)


button_1 = tk.Button(master=frame, text='1', padx=15,
                     pady=5, width=3, command=lambda: myclick(1))
button_1.grid(row=1, column=0, pady=2)
button_2 = tk.Button(master=frame, text='2', padx=15,
                     pady=5, width=3, command=lambda: myclick(2))
button_2.grid(row=1, column=1, pady=2)
button_3 = tk.Button(master=frame, text='3', padx=15,
                     pady=5, width=3, command=lambda: myclick(3))
button_3.grid(row=1, column=2, pady=2)
button_4 = tk.Button(master=frame, text='4', padx=15,
                     pady=5, width=3, command=lambda: myclick(4))
button_4.grid(row=2, column=0, pady=2)
button_5 = tk.Button(master=frame, text='5', padx=15,
                     pady=5, width=3, command=lambda: myclick(5))
button_5.grid(row=2, column=1, pady=2)
button_6 = tk.Button(master=frame, text='6', padx=15,
                     pady=5, width=3, command=lambda: myclick(6))
button_6.grid(row=2, column=2, pady=2)
button_7 = tk.Button(master=frame, text='7', padx=15,
                     pady=5, width=3, command=lambda: myclick(7))
button_7.grid(row=3, column=0, pady=2)
button_8 = tk.Button(master=frame, text='8', padx=15,
                     pady=5, width=3, command=lambda: myclick(8))
button_8.grid(row=3, column=1, pady=2)
button_9 = tk.Button(master=frame, text='9', padx=15,
                     pady=5, width=3, command=lambda: myclick(9))
button_9.grid(row=3, column=2, pady=2)
button_0 = tk.Button(master=frame, text='0', padx=15,
                     pady=5, width=3, command=lambda: myclick(0))
button_0.grid(row=4, column=1, pady=2)

button_add = tk.Button(master=frame, text="+", padx=15,
                       pady=5, width=3, command=lambda: myclick('+'))
button_add.grid(row=1, column=4, pady=2)

button_subtract = tk.Button(
    master=frame, text="-", padx=15, pady=5, width=3, command=lambda: myclick('-'))
button_subtract.grid(row=2, column=4, pady=2)

button_multiply = tk.Button(
    master=frame, text="*", padx=15, pady=5, width=3, command=lambda: myclick('*'))
button_multiply.grid(row=3, column=4, pady=2)

button_div = tk.Button(master=frame, text="/", padx=15,
                       pady=5, width=3, command=lambda: myclick('/'))
button_div.grid(row=4, column=4, pady=2)

button_clear = tk.Button(master=frame, text="clear",
                         padx=5, pady=5, width=9, command=clear)
button_clear.grid(row=6, column=0, pady=2)

button_equal = tk.Button(master=frame, text="=", padx=15,
                         pady=5, width=9, command=answer)
button_equal.grid(row=6, column=3, pady=2)

# Execute Tkinter
root.mainloop()
