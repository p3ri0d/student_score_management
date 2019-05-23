from tkinter import *
from tkinter.messagebox import *

from sql_connetion import *


check_name = ""


# 判断当前用户
class Flag_1(object):
    def __init__(self, name):
        self.name = name
        self.check(self.name)

    def check(self, name):
        global check_name
        check_name = name


# 增
class InputFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)
        self.e4 = Entry(self)
        self.create_page()

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

    def write(self, name, num, course, score):
        sql = "insert into score_info(stu_name, stu_num, course_name, course_score) values ('{}','{}','{}','{}')".format(str(name), str(num), str(course), str(score))

        try:
            cursor.execute(sql)
            db.commit()
            showinfo(title="提示", message="写入成功")
        except:
            db.rollback()
            showinfo(title="提示", message="写入失败")

    def click(self):
        name = self.e1.get()
        num = self.e2.get()
        course = self.e3.get()
        score = self.e4.get()

        if self.is_space(name) or self.is_space(num) or self.is_space(course) or self.is_space(score):
            showinfo(title='提示', message="输入项为空")
        else:
            self.write(name, num, course, score)

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)

        Label(self, text='姓名: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1, column=1, stick=E)

        Label(self, text='学号: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)

        Label(self, text='科目: ').grid(row=3, stick=W, pady=10)
        self.e3.grid(row=3, column=1, stick=E)

        Label(self, text='成绩: ').grid(row=4, stick=W, pady=10)
        self.e4.grid(row=4, column=1, stick=E)

        Button(self, text='录入', command=self.click).grid(row=6, column=1, stick=E, pady=10)


# 删
class DeleteFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.create_page()

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

    def delete(self, num, course):
        sql = "delete from score_info where stu_num={} and course_name={}".format(str(num), str(course))

        if cursor.execute(sql):
            db.commit()
            showinfo(title="提示", message="删除成功")
        else:
            db.rollback()
            showinfo(title="提示", message="删除失败，请输入正确的学号和课程名")

    def click(self):
        num = self.e1.get()
        course = self.e2.get()

        if self.is_space(num)or self.is_space(course):
            showinfo(title='提示', message="输入项为空")
        else:
            self.delete(num, course)

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)

        Label(self, text='学号: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1, column=1, stick=E)

        Label(self, text='课程名: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)

        Button(self, text='删除', command=self.click).grid(row=6, column=1, stick=E, pady=10)


# 改
class ModifyFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)

        self.create_page()

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

    def modify(self, num, course, score):
        sql = "update score_info set course_name={},course_score={} where stu_num={}".format(str(course), str(score), str(num))

        if cursor.execute(sql):
            db.commit()
            showinfo(title="提示", message="修改成功")
        else:
            db.rollback()
            showinfo(title="提示", message="修改失败，请输入正确的学号和课程名")

    def click(self):
        num = self.e1.get()
        course = self.e2.get()
        score = self.e3.get()

        if self.is_space(num) or self.is_space(course) or self.is_space(score):
            showinfo(title='提示', message="输入项为空")
        else:
            self.modify(num, course, score)

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='学号: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1, column=1, stick=E)

        Label(self, text='课程名: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)

        Label(self, text='成绩: ').grid(row=3, stick=W, pady=10)
        self.e3.grid(row=3, column=1, stick=E)

        Button(self, text='修改', command=self.click).grid(row=4, column=1, stick=E, pady=10)


# 查
class QueryFrame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.root = master
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.create_page()

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

    def query(self, num, course):
        sql = "select * from score_info where stu_num='{}' and course_name='{}'".format(str(num), str(course))
        # print(sql)

        if cursor.execute(sql):
            res = cursor.fetchall()
            for i in res:
                course_name = i[1]
                stu_name = i[2]
                stu_num = i[3]
                course_score = i[4]
            message = "姓名：{} \n学号：{}\n课程名：{}\n成绩：{}\n".format(stu_name, stu_num, course_name, course_score)

            showinfo(title="结果", message=message)

        else:
            db.rollback()
            showinfo(title="提示", message="查找失败，请输入正确的学号和课程名")

    def click(self):
        num = self.e1.get()
        course = self.e2.get()

        if self.is_space(num) or self.is_space(course):
            showinfo(title='提示', message="输入项为空")
        else:
            self.query(num, course)

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)

        Label(self, text='学号: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1, column=1, stick=E)

        Label(self, text='课程名: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)

        Button(self, text='查找', command=self.click).grid(row=6, column=1, stick=E, pady=10)


# 老师修改密码
class UpdateFrame_teach(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.e1 = Entry(self)
        self.e2 = Entry(self)

        self.create_page()

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

    def update_pass(self, password, username):
        if check_name == username:
            sql = "update teach_user set password={} where teacher_num={}".format(str(password), str(username))
            if cursor.execute(sql):
                db.commit()
                showinfo(title="提示", message="修改成功")
            else:
                db.rollback()
                showinfo(title="提示", message="修改失败")
        else:
            showinfo(title="提示", message="请输入自己的账号")
            return 0

    def click(self):
        password = self.e1.get()
        username = self.e2.get()

        if self.is_space(password) or self.is_space(username):
            showinfo(title='提示', message="输入项为空")
        else:
            self.update_pass(password, username)

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='新密码: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1, column=1, stick=E)
        Label(self, text='用户名: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)

        Button(self, text='修改', command=self.click).grid(row=3, column=1, stick=E, pady=10)


# 学生修改密码
class UpdateFrame_stu(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.e1 = Entry(self)
        self.e2 = Entry(self)

        self.create_page()

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

    def update_pass(self, password, username):
        if check_name == username:
            sql = "update stu_user set password={} where stu_num={}".format(str(password), str(username))
            if cursor.execute(sql):
                db.commit()
                showinfo(title="提示", message="修改成功")
            else:
                db.rollback()
                showinfo(title="提示", message="修改失败")
        else:
            showinfo(title="提示", message="请输入自己的账号")
            return 0

    def click(self):
        password = self.e1.get()
        username = self.e2.get()

        if self.is_space(password) or self.is_space(username):
            showinfo(title='提示', message="输入项为空")
        else:
            self.update_pass(password, username)

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='新密码: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1, column=1, stick=E)
        Label(self, text='用户名: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)

        Button(self, text='修改', command=self.click).grid(row=3, column=1, stick=E, pady=10)


# 信息统计
class StatisticsFrame(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.e1 = Entry(self)
        self.e2 = Entry(self)
        self.e3 = Entry(self)
        self.e4 = Entry(self)
        self.e5 = Entry(self)
        self.create_page()

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

    def query_ac(self, ac):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where ac='{}'".format(str(ac))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        showinfo(title="结果", message="不及格人数为：{}".format(str(no_pass)))

    def query_major(self, major):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where major='{}'".format(str(major))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}".format(str(no_pass))
        showinfo(title="结果", message=message)

    def query_class(self, stu_class):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where class='{}'".format(str(stu_class))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}".format(str(no_pass))
        showinfo(title="结果", message=message)

    def query_ac_major(self, ac, major):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where ac='{}' and major='{}'".format(str(ac), str(major))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}".format(str(no_pass))
        showinfo(title="结果", message=message)

    def query_ac_stu_class(self, ac, stu_class):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where ac='{}' and class='{}'".format(str(ac), str(stu_class))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}".format(str(no_pass))
        showinfo(title="结果", message=message)

    def query_major_stu_class(self, major, stu_class):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where major='{}' and class='{}'".format(str(major), str(stu_class))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}".format(str(no_pass))
        showinfo(title="结果", message=message)

    def query_list(self, ac, major, stu_class):
        f = open("data.txt", 'a')
        title = "course_name;stu_name;stu_num;course_score"
        f.write(title)
        f.write("\n")

        sql = "select stu_num from stu_info where ac='{}' and major='{}' and class='{}'".format(str(ac), str(major), str(stu_class))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}'".format(t[i][0])
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            new_snake = snake[1:]
                            score_list.append(int(snake[1:][3]))
                            aim_string = ';'.join(new_snake)
                            # print(aim_string)
                            f.write(aim_string)
                            f.write("\n")
                            flag = flag - 1
                    for k in score_list:
                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}".format(str(no_pass))
        showinfo(title="结果", message=message)

    def click_1(self):
        ac = self.e1.get()
        major = self.e2.get()
        stu_class = self.e3.get()

        if (not self.is_space(ac)) and self.is_space(major) and self.is_space(stu_class):
            self.query_ac(ac)
            return 1
        if (not self.is_space(major)) and self.is_space(ac) and self.is_space(stu_class):
            self.query_major(major)
            return 1
        if (not self.is_space(stu_class)) and self.is_space(ac) and self.is_space(major):
            self.query_class(stu_class)
            return 1
        if (not self.is_space(stu_class)) and (not self.is_space(ac)) and self.is_space(major):
            self.query_ac_stu_class(ac, stu_class)
            return 1
        if (not self.is_space(stu_class)) and self.is_space(ac) and (not self.is_space(major)):
            self.query_major_stu_class(major, stu_class)
            return 1
        if self.is_space(stu_class) and (not self.is_space(ac)) and (not self.is_space(major)):
            self.query_ac_major(ac, major)
            return 1
        if (not self.is_space(stu_class)) and (not self.is_space(ac)) and (not self.is_space(major)):
            self.query_list(ac, major, stu_class)
            return 1
        if self.is_space(stu_class) or self.is_space(ac) or self.is_space(major):
            showinfo(title="提示", message="输入不能全为空")

    def select_all(self, course_name, major):
        sql = "select stu_num from stu_info where major='{}'".format(str(major))
        n = cursor.execute(sql)
        no_pass = 0

        if n:
            t = cursor.fetchall()
            for i in range(len(t)):
                sql_2 = "select * from score_info where stu_num='{}' and course_name='{}'".format(t[i][0], course_name)
                # print(sql_2)
                # print(t[i][0])
                x_num = cursor.execute(sql_2)
                if x_num:
                    flag = x_num
                    score_list = []
                    sum_score = 0
                    # print(flag)
                    if flag:
                        x_temp = cursor.fetchall()
                        for j in range(len(x_temp)):
                            snake = x_temp[j]
                            score_list.append(int(snake[1:][3]))
                            flag = flag - 1
                    for k in score_list:
                        sum_score = sum_score + k
                        avg_score = sum_score / len(score_list)

                        max_score = max(score_list)
                        min_score = min(score_list)

                        if k < 60:
                            no_pass = no_pass + 1
                else:
                    showinfo(title='提示', message='{}没有结果。'.format(str(t[i][0])))

        else:
            showinfo(title='提示', message='没有结果！')
        message = "不及格人数为：{}\n 平均分为：{}\n 最高分为：{}\n 最低分为：{}".format(str(no_pass), str(avg_score), str(max_score), str(min_score))
        showinfo(title="结果", message=message)

    def click_2(self):
        course_name = self.e4.get()
        major = self.e5.get()

        if self.is_space(course_name) or self.is_space(major):
            showinfo(title='提示', message="输入项为空")
        else:
            self.select_all(course_name, major)

    def create_page(self):
        Label(self, text='请输入查询内容').grid(row=0, stick=W, pady=10)
        Label(self, text='院系: ').grid(row=1, stick=W, pady=10)
        self.e1.grid(row=1,  column=1, stick=E)
        Label(self, text='专业: ').grid(row=2, stick=W, pady=10)
        self.e2.grid(row=2, column=1, stick=E)
        Label(self, text='班级: ').grid(row=3, stick=W, pady=10)
        self.e3.grid(row=3, column=1, stick=E)
        Button(self, text='查询统计信息', command=self.click_1).grid(row=4, column=1, stick=E, pady=10)
        Label(self, text='学科：').grid(row=5, stick=W, pady=10)
        self.e4.grid(row=5, column=1, stick=E)
        Label(self, text='专业：').grid(row=6, stick=W, pady=10)
        self.e5.grid(row=6, column=1, stick=E)
        Button(self, text='查询分数分布', command=self.click_2).grid(row=7, column=1, stick=E, pady=10)
