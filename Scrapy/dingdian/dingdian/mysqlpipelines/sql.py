# -*- coding: utf-8 -*-
import pymysql
from dingdian import settings

db_host = settings.MYSQL_HOST
db_user = settings.MYSQL_USER
db_pwd = settings.MYSQL_PASSWORD
db_data = settings.MYSQL_DB

db = pymysql.connect(db_host, db_user, db_pwd, db_data, charset="utf8")
cursor = db.cursor()

class SQL:

    @classmethod
    def insert_bookinfo(cls, xs_name, xs_author, bookid, category, status, updatetime):
        sql = "INSERT INTO ddbook(`xs_name`,`xs_author`, `bookid`, `category`, `status`, `updatetime`) VALUES(%(xs_name)s, %(xs_author)s, %(bookid)s, %(category)s , %(status)s, %(updatetime)s)"

        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'bookid': bookid,
            'category': category,
            'status': status,
            'updatetime': updatetime,
        }
        cursor.execute(sql, value)
        db.commit()

    @classmethod
    def select_book(cls, bookid):
        sql = "SELECT EXISTS(SELECT 1 FROM ddbook WHERE bookid=%(bookid)s)"
        value = {
            'bookid': bookid
        }
        cursor.execute(sql, value)
        return cursor.fetchall()[0][0]

    @classmethod
    def select_chapter(cls, url):
        sql = "SELECT EXISTS(SELECT 1 FROM dd_chaptername WHERE url=%(url)s)"
        value = {
            'url': url
        }
        cursor.execute(sql, value)
        return cursor.fetchall()[0][0]

    @classmethod
    @classmethod
    def insert_chapterinfo(cls, xs_chaptername, xs_content, book_id, num_id, url):
        sql = "INSERT INTO ddbook(`xs_chaptername`,`xs_content`, `book_id`, `num_id`, `status`, `updatetime`) VALUES(%(xs_name)s, %(xs_author)s, %(bookid)s, %(category)s , %(status)s, %(updatetime)s)"

        value = {
            'xs_name': xs_name,
            'xs_author': xs_author,
            'bookid': bookid,
            'category': category,
            'status': status,
            'updatetime': updatetime,
        }
        cursor.execute(sql, value)
        db.commit()

a = SQL.select_chapter("https://www.x23us.com/html/66/66938/27683036.html")
print(a)
# a = "1234"
# print(a[:2])