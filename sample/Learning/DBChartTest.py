#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# Open connection
db = MySQLdb.connect("localhost", "x", "x", "TESTDB", charset='utf8' )

# Get cursor
cursor = db.cursor()

# Drop table
cursor.execute("DROP TABLE")

# Create table
# sql = """CREATE TABLE Courses (
#          Timekey  CHAR(20) NOT NULL,
#         Coursename  CHAR(20),
#			Actual number (5))

# Insert
#sql = "INSERT INTO Courses(Timekey, \
#       Coursename) \
#       VALUES (%s, %s)" % \
#       ('...', '...')

#Search
#sql = "SELECT * FROM Courses \
#       WHERE ... > %s" % (1000)

#Update
# sql = "UPDATE Courses SET ... = ... + 1 WHERE ... = '%c'" % ('...')

#Delete
#sql = "DELETE FROM Courses WHERE .. > %s" % (..)

try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# Disconnect
db.close()
