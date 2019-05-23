import pymysql


db = pymysql.connect('localhost', 'root', 'root', 'score_management')
cursor = db.cursor()