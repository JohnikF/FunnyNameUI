import tkinter as tk
import random

first_names = []
second_names = []

window = tk.Tk()
window.geometry("800x400")
window.title("Funny Names")
window.configure(bg="green")

def add1():
    text = entry_1.get()
    if text == "":
        return

    entry_1.delete(0,"end")
    first_names.append(text)
    text_list = ""
    for i in first_names:
        text_list += f"{i}\n"
    list_label_1["text"] = text_list

def add2():
    text = entry_2.get()
    if text == "":
        return

    entry_2.delete(0, "end")
    second_names.append(text)
    text_list = ""
    for i in second_names:
        text_list += f"{i}\n"
    list_label_2["text"] = text_list

def launch():
    name_1 = random.choice(first_names)
    name_2 = random.choice(second_names)
    names = name_1 + " " + name_2
    label_name["text"] = names




button_add_1 = tk.Button(window, width=10, height=3, bg="black", fg="light green", text="Add", command=add1)
button_add_1.place(x=100, y=50 )

button_add_2 = tk.Button(window, width=10, height=3, bg="black", fg="light green", text="Add", command=add2)
button_add_2.place(x=550, y=50)

entry_1 = tk.Entry(window, width=15, bg="black", fg="light green")
entry_1.place(x=97, y=150)

list_label_1 = tk.Label(window, bg="black", fg="light green", text="Empty List", width=13, height=10)
list_label_1.place(x=97, y=190)

entry_2 = tk.Entry(window, width=15, bg="black", fg="light green")
entry_2.place(x=547, y=150)

list_label_2 = tk.Label(window, bg="black", fg="light green", text="Empty List", width=13, height=10)
list_label_2.place(x=547, y=190)

launch_btn = tk.Button(window, width=15, height=2, bg="black", fg="light green", text="Launch", command=launch)
launch_btn.place(x=325, y=200)

label_name = tk.Label(window, text="You today are...", width=15, height=5, bg="green",font=("Arial",15))
label_name.place(x=300, y=50)




window.mainloop()