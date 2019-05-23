from tkinter import *
from tkinter.messagebox import *
from main_page import *
from main_page import Flag

from sql_connetion import *


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        self.root.geometry('400x400')
        self.username = StringVar()
        self.password = StringVar()
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)
        self.page.pack()

        Label(self.page).grid(row=0, stick=W)
        # add user_id
        Label(self.page, text='用户名：').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)

        # add user_password
        Label(self.page, text='密   码：').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)

        # add stu button
        Button(self.page, text="学生登录", command=self.stu_login).grid(row=3, stick=W, pady=10)

        # add teach button
        Button(self.page, text="老师登录", command=self.teach_login).grid(row=3, column=1)

        # add exit button
        Button(self.page, text="退出", command=self.page.quit).grid(row=3, column=2, stick=E)

    def stu_login(self):
        user_id = self.username.get()
        password = self.password.get()
        Flag(self.username.get())

        if self.is_space(user_id) or self.is_space(password):
            showinfo(title="提示", message="用户名或密码不为空")
            return 0

        sql = "select * from stu_user where stu_num=" + str(user_id) + " and password=" + str(password)
        cursor.execute(sql)

        if cursor.fetchall():
            self.page.destroy()
            MainPage_stu(self.root)
        else:
            showinfo(title="错误", message="账号或密码错误")

    def teach_login(self):
        user_id = self.username.get()
        password = self.password.get()
        Flag(self.username.get())

        if self.is_space(user_id) or self.is_space(password):
            showinfo(title="提示", message="用户名或密码不为空")
            return 0

        sql = "select * from teach_user where teacher_num=" + str(user_id) + " and password=" + str(password)
        cursor.execute(sql)

        if cursor.fetchall():
            self.page.destroy()
            MainPage_teach(self.root)
        else:
            showinfo(title="错误", message="账号或密码错误")

    def is_space(self, text):
        temp = 0
        for i in text:
            if not i.isspace():
                temp = 1
                break
        if temp == 1:
            return 0
        else:
            return 1
