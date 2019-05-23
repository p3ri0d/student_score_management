import sys
from tkinter import *
from view_page import *


class MainPage_teach(object):

    def __init__(self, master=None):
        self.root = master
        self.root.geometry("600x400")
        self.create_page()

    def create_page(self):
        self.input_page = InputFrame(self.root)
        self.delete_page = DeleteFrame(self.root)
        self.modify_page = ModifyFrame(self.root)
        self.query_page = QueryFrame(self.root)
        self.update_page = UpdateFrame_teach(self.root)
        self.statistics_page = StatisticsFrame(self.root)

        self.input_page.pack()

        menu_bar = Menu(self.root)
        menu_bar.add_command(label='增加成绩', command=self.input_data)
        menu_bar.add_command(label='删除成绩', command=self.delete_data)
        menu_bar.add_command(label='修改成绩', command=self.modify_data)
        menu_bar.add_command(label='查讯成绩', command=self.query_data)
        menu_bar.add_command(label='修改密码', command=self.update_data)
        menu_bar.add_command(label='信息统计', command=self.statistics_data)
        self.root['menu'] = menu_bar

    def input_data(self):
        self.input_page.pack()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.modify_page.pack_forget()
        self.update_page.pack_forget()
        self.statistics_page.pack_forget()

    def delete_data(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack()
        self.modify_page.pack_forget()
        self.update_page.pack_forget()
        self.statistics_page.pack_forget()

    def modify_data(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.modify_page.pack()
        self.update_page.pack_forget()
        self.statistics_page.pack_forget()

    def query_data(self):
        self.input_page.pack_forget()
        self.query_page.pack()
        self.delete_page.pack_forget()
        self.modify_page.pack_forget()
        self.update_page.pack_forget()
        self.statistics_page.pack_forget()

    def update_data(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.modify_page.pack_forget()
        self.update_page.pack()
        self.statistics_page.pack_forget()

    def statistics_data(self):
        self.input_page.pack_forget()
        self.query_page.pack_forget()
        self.delete_page.pack_forget()
        self.modify_page.pack_forget()
        self.update_page.pack_forget()
        self.statistics_page.pack()


class MainPage_stu(object):

    def __init__(self, master=None):
        self.root = master
        self.root.geometry("600x400")
        self.create_page()

    def create_page(self):
        self.query_page = QueryFrame(self.root)
        self.update_page = UpdateFrame_stu(self.root)
        self.statistics_page = StatisticsFrame(self.root)

        self.query_page.pack()

        menu_bar = Menu(self.root)
        menu_bar.add_command(label='查讯成绩', command=self.query_data)
        menu_bar.add_command(label='修改密码', command=self.update_data)
        menu_bar.add_command(label='信息统计', command=self.statistics_data)
        self.root['menu'] = menu_bar

    def query_data(self):
        self.query_page.pack()
        self.update_page.pack_forget()
        self.statistics_page.pack_forget()

    def update_data(self):
        self.query_page.pack_forget()
        self.update_page.pack()
        self.statistics_page.pack_forget()

    def statistics_data(self):
        self.query_page.pack_forget()
        self.update_page.pack_forget()
        self.statistics_page.pack()


class Flag(object):
    def __init__(self, name):
        Flag_1(name)

