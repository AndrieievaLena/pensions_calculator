# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import tkinter
from tkinter import ttk
from tkinter import messagebox

main = tkinter.Tk()

p_var = tkinter.StringVar()
choice_var = tkinter.StringVar()


def button_click():
    pension = int(p_var.get())
    messagebox.showinfo("Результат", "Нарахована пенсія - " + str(pension))
    min_zar = int(choice_var.get())
    if pension <= 3 * min_zar:
        podatok = 0
    elif pension > 10 * min_zar:
        pension -= 3 * min_zar
        if pension < 10 * min_zar:
            podatok: float = pension * 0.15
        else:
            podatok: float = 10 * min_zar * 0.15
        pension -= 10 * min_zar
        if pension > 0:
            podatok += pension * 0.2
    else:
        podatok = (pension - 3 * min_zar) * 0.15
    messagebox.showinfo("Результат", "Податок -" + str(podatok))

labell = tkinter.Label(text='Розмір пенсії')
labell.pack()
edit = tkinter.Entry(main, textvariable=p_var)
edit.pack()
labell2 = tkinter.Label(text="Мінімальна заробітна плата")
labell2.pack()
choice = ttk.Combobox(main, textvariable=choice_var)
choice["values"] = ("1378", "1450", "1550")
choice.pack()
button = tkinter.Button(main, text="Розрахувати", command=button_click)
button.pack()
main.mainloop()
