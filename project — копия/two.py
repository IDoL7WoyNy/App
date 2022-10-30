import tkinter as tk
import pymysql
import time
import runpy

f = open("school.txt")
for i in f:
    school = i

mark = 0


def backing():
    app.destroy()
    time.sleep(1)
    runpy.run_module("second")


def one():
    global mark
    mark = 1


def two():
    global mark
    mark = 2


def three():
    global mark
    mark = 3


def four():
    global mark
    mark = 4


def five():
    global mark
    mark = 5


def posting():
    try:
        connection = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database=school,
            cursorclass=pymysql.cursors.DictCursor)
        if mark != 0:
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO marks (name, mark,offer ) VALUES ('{}','{}','{}')".format(name, mark,
                                                                                                      entry_1.get())
                cursor.execute(insert_query)
                connection.commit()
                app.destroy()
                time.sleep(1)
                runpy.run_module("second")
    except:
        print("error")


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
photo_6 = tk.PhotoImage(file="VB.png")
photo_7 = tk.PhotoImage(file="B.png")
photo_8 = tk.PhotoImage(file="M.png")
photo_9 = tk.PhotoImage(file="G.png")
photo_10 = tk.PhotoImage(file="VG.png")
btn1 = tk.Button(text="Назад", bg="#F4A289", image=photo_6, height=30, width=30, bd=0, command=one)
btn2 = tk.Button(text="Назад", bg="#F4A289", image=photo_7, height=30, width=30, bd=0, command=two)
btn3 = tk.Button(text="Назад", bg="#F4A289", image=photo_8, height=30, width=30, bd=0, command=three)
btn4 = tk.Button(text="Назад", bg="#F4A289", image=photo_9, height=30, width=30, bd=0, command=four)
btn5 = tk.Button(text="Назад", bg="#F4A289", image=photo_10, height=30, width=30, bd=0, command=five)

lable_1 = tk.Button(text="Назад", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff", justify=tk.LEFT, bd=0,
                    height=1, command=backing,anchor="center")

lable_2 = tk.Label(text="Название", bg="#F4A289", font=("Arial", 18, "underline"), fg="#ffffff", justify=tk.LEFT, bd=0,
                   height=2,anchor="center")
lable_3 = tk.Label(text="Калории", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff", justify=tk.LEFT , bd=0,
                   height=2, anchor="w")
lable_4 = tk.Label(text="Масса", bg="#F4A289", font=("Arial", 18, "bold"), fg="#ffffff", justify=tk.LEFT, bd=0,
                   height=2, anchor="w")
lable_9 = tk.Label(text="Описание", bg="#F4A289", font=("Arial", 7, "underline"), fg="#ffffff", justify=tk.LEFT, bd=0,
                   height=2, anchor="w")
lable_10 = tk.Button(text="Отправить отзыв", bg="#F4A289", font=("Arial", 10, "bold"), fg="#ffffff", justify=tk.CENTER,
                     bd=0, height=1, command=posting)

lable_1.grid(row=1, column=0, pady=20, columnspan=5)

lable_9.grid(row=5, column=0, stick="we", columnspan=5, pady=10)

lable_2.grid(row=2, column=0, stick="we", columnspan=5)
lable_3.grid(row=3, column=0, stick="we", columnspan=5)
lable_4.grid(row=4, column=0, stick="we", columnspan=5)
btn1.grid(row=6, column=0)
btn2.grid(row=6, column=1)
btn3.grid(row=6, column=2)
btn4.grid(row=6, column=3)
btn5.grid(row=6, column=4)
entry_1.grid(row=7, column=0, stick="we", columnspan=5, pady=10, rowspan=3,padx=25)
lable_10.grid(row=10, column=0, stick="we", columnspan=5)

try:
    connection = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="root",
        database=school,
        cursorclass=pymysql.cursors.DictCursor)
    with connection.cursor() as cursor:
        select_all_rows = "SELECT name FROM products WHERE id=2"
        cursor.execute(select_all_rows)
        name_new = cursor.fetchone()
        name = name_new["name"]
    with connection.cursor() as cursor:
        select_all_rows = "SELECT calories FROM products WHERE id=2"
        cursor.execute(select_all_rows)
        calories_new = cursor.fetchone()
        calories = calories_new["calories"]
    with connection.cursor() as cursor:
        select_all_rows = "SELECT masse FROM products WHERE id=2"
        cursor.execute(select_all_rows)
        masse_new = cursor.fetchone()
        masse = masse_new["masse"]
    with connection.cursor() as cursor:
        select_all_rows = "SELECT recipe FROM products WHERE id=2"
        cursor.execute(select_all_rows)
        recipe_new = cursor.fetchone()
        recipe = recipe_new["recipe"]
    calories = "Калорийность:" + str(calories) + "кКал"
    masse = "Масса:" + str(masse) + "г"
    lable_2["text"] = name
    lable_3["text"] = calories
    lable_4["text"] = masse
    lable_9["text"] = recipe
except:
    print("error")
app.mainloop()
