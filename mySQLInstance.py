# coding:utf-8
import MySQLdb

def initDbConnection():
    conn = MySQLdb.connect(host='localhost', user='root', passwd='root', db='legalminer', port=3306, charset='utf8')
    return conn
