import tkinter as tk
import pymysql
import time
import runpy




def pressing_one():
    app.destroy()
    time.sleep(1)
    runpy.run_module("one")
def pressing_two():
    app.destroy()
    time.sleep(1)
    runpy.run_module("two")
def pressing_three():
    app.destroy()
    time.sleep(1)
    runpy.run_module("three")
def pressing_four():
    app.destroy()
    time.sleep(1)
    runpy.run_module("four")


app = tk.Tk()
ico = tk.PhotoImage(file="ico.png")
app.iconphoto(False,ico)
app.title("CheckFOOD")
app.geometry("300x500+600+150")
app.resizable(width=False, height=False)
app.config(bg="#F4A289")
photo_1 = tk.PhotoImage(file="name.png")
photo_2 = tk.PhotoImage(file="first.png")
photo_3 = tk.PhotoImage(file="second.png")
photo_4 = tk.PhotoImage(file="snacks.png")
photo_5 = tk.PhotoImage(file="drinks.png")

entry_1 = tk.Entry(background="#F4A289")
entry_2 = tk.Entry(background="#F4A289")
entry_3 = tk.Entry(background="#F4A289")


lable_1 = tk.Label(image=photo_1, bg="#F4A289")

lable_2 = tk.Button(text="Первое", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff",justify=tk.LEFT,bd=0,height=2,command=pressing_one)
lable_3 = tk.Button(text="Второе", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff",justify=tk.LEFT,bd=0,height=2,command=pressing_two)
lable_4 = tk.Button(text="Закуски", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff",justify=tk.LEFT,bd=0,height=2,command=pressing_three)
lable_9 = tk.Button(text="Напитки", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff",justify=tk.LEFT,bd=0,height=2,command=pressing_four)


lable_5= tk.Button(image=photo_2, bg="#F4A289",bd=0,command=pressing_one)
lable_6=tk.Button(image=photo_3, bg="#F4A289",bd=0,command=pressing_two)
lable_7=tk.Button(image=photo_4, bg="#F4A289",bd=0,command=pressing_three)
lable_8=tk.Button(image=photo_5, bg="#F4A289",bd=0,command=pressing_four)

lable_1.grid(row=1, column=0, padx=40, pady=50, columnspan=2)
lable_5.grid(row=2, column=1)
lable_6.grid(row=3, column=1, pady=10)
lable_7.grid(row=4, column=1)
lable_8.grid(row=5, column=1)
lable_9.grid(row=5,column=0,stick="we",pady=10,padx=10)

lable_2.grid(row=2, column=0,stick="we",padx=10)
lable_3.grid(row=3, column=0, pady=6,stick="we",padx=10)
lable_4.grid(row=4, column=0,stick="we",padx=10)




app.mainloop()
