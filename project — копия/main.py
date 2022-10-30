import tkinter as tk
import pymysql
import time
import runpy

school = ""


def pressing_login():
    global school
    if entry_1.get() and entry_2.get() and entry_3.get():
        school = entry_1.get()
        school = "№" + school
        login = entry_2.get()
        password = entry_3.get()
        try:
            connection = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database=school,
                cursorclass=pymysql.cursors.DictCursor)

            with connection.cursor() as cursor:
                select_all_rows = "SELECT password FROM users WHERE name=('{}')".format(login)
                cursor.execute(select_all_rows)
                password_new = cursor.fetchone()
                password_new = password_new["password"]
                if password == password_new:
                    lable_5["text"] = "Good login"
                    app.destroy()
                    f = open("school.txt", "w")
                    f.write(school)
                    f.close()
                    time.sleep(1)
                    runpy.run_module("second")




                else:
                    lable_5["text"] = "invalid login/password/school"

        except:
            lable_5["text"] = "invalid login/password/school"

    else:
        lable_5["text"] = "invalid login/password/school"


def pressing_reg():
    massive_of_logins = []
    if entry_1.get() and entry_2.get() and entry_3.get():
        school = entry_1.get()
        school = "№" + school
        login = entry_2.get()
        password = entry_3.get()
        entry_1.delete(0, "end")
        entry_2.delete(0, "end")
        entry_3.delete(0, "end")
        try:
            connection = pymysql.connect(
                host="localhost",
                port=3306,
                user="root",
                password="root",
                database=school,
                cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                select_all_rows = "SELECT name FROM `users`"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for i in rows:
                    massive_of_logins.append((i["name"]))
            if login not in massive_of_logins:
                try:
                    with connection.cursor() as cursor:
                        insert_query = "INSERT INTO users (name, password) VALUES ('{}','{}')".format(login, password)
                        cursor.execute(insert_query)
                        connection.commit()
                    with connection.cursor() as cursor:
                        select_all_rows = "SELECT name FROM `users`"
                        cursor.execute(select_all_rows)
                        rows = cursor.fetchall()
                        for i in rows:
                            massive_of_logins.append((i["name"]))
                except:
                    lable_5["text"] = "invalid login/password/school"
            else:
                lable_5["text"] = "invalid login/password"

        except:
            lable_5["text"] = "invalid login/password/school"



app = tk.Tk()
ico = tk.PhotoImage(file="ico.png")
app.iconphoto(False,ico)
app.title("CheckFOOD")
app.geometry("300x500+600+150")
app.resizable(width=False, height=False)
app.config(bg="#F4A289")
photo_1 = tk.PhotoImage(file="name.png")
entry_1 = tk.Entry(background="#F4A289")
entry_2 = tk.Entry(background="#F4A289")
entry_3 = tk.Entry(background="#F4A289")

button_1 = tk.Button(text="Войти", bg="#F4A289", font=("Arial", 15, "bold"), fg="#ffffff", bd=0, command=pressing_login)
button_2 = tk.Button(text="Зарегестрироваться", bg="#F4A289", font=("Arial", 15, "bold"), fg="#ffffff", bd=0,
                     command=pressing_reg)

lable_1 = tk.Label(image=photo_1, bg="#F4A289")

lable_2 = tk.Label(text="Школа", bg="#F4A289", font=("Arial", 15, "bold"), fg="#ffffff")
lable_3 = tk.Label(text="Логин", bg="#F4A289", font=("Arial", 15, "bold"), fg="#ffffff")
lable_4 = tk.Label(text="Пароль", bg="#F4A289", font=("Arial", 15, "bold"), fg="#ffffff")
lable_5 = tk.Label(text="", bg="#F4A289", font=("Arial", 10, "bold"), fg="#ffffff")

lable_1.grid(row=1, column=0, padx=40, pady=50, columnspan=2)
entry_1.grid(row=2, column=1)
entry_2.grid(row=3, column=1, pady=10)
entry_3.grid(row=4, column=1)

lable_2.grid(row=2, column=0)
lable_3.grid(row=3, column=0, pady=6)
lable_4.grid(row=4, column=0)
lable_5.grid(row=7, column=0, columnspan=2, stick="we", pady=10)

button_1.grid(row=5, column=0, columnspan=2, stick="we", pady=10)
button_2.grid(row=6, column=0, columnspan=2, stick="we")

app.mainloop()
