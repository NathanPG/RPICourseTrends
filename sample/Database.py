import mysql.connector
from mysql.connector import errorcode
import string


class CourseDb(object):
    def __init__(self, my_user,my_password, my_host, my_database ):
        self.cnx = mysql.connector.connect(
            user=my_user,
            password=my_password,
            host=my_host,
            database=my_database
        )

        self.database = my_database

        self.cursor = self.cnx.cursor()

        try:
            # try to connect to database
            self.cnx.database = my_database
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database(my_database)
                self.cnx.database = my_database
            else:
                print(err)
                exit(1)

    def create_database(self, my_database):
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(my_database))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def create_table_other(self,table_name, command):
        try:
            print("Creating table {}: ".format(table_name), end='')
            self.cursor.execute(command)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    def show_database(self):
        query = "show databases;"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def show_tables(self,database):
        self.cursor.execute("use {};".format(database))
        self.cursor.execute("show tables;")
        return self.cursor.fetchall()

    def drop_database(self,database):
        query = "DROP DATABASE {};".format(database)
        self.cursor.execute(query)

    def drop_table(self,table):
        try:
            query = "DROP TABLE {}".format(table)
            self.cursor.execute(query)
            print("Success to drop table {} from database {}".format(table, self.database))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)

    def create_tables(self, table_name, element, key):
        # table = "Courses2"
        query = "CREATE TABLE {} (".format(table_name)
        for item in element:
            query += " {} {} , ".format(item[0], item[1])
        query += "PRIMARY KEY ({}) )".format(key)
        try:
            print("Creating table {}: ".format(table_name), end='')
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
        self.cnx.commit()

    """
    [('time', 'datetime', 'NO', 'PRI', None, ''), ('comments', 'varchar(11)', 'YES', '', None, '')]
    [ (column1, type, Null, keyOrNot, None, "), (), () ]
    """

    def describe_table(self,table):
        query = "DESCRIBE {:s}; ".format(table)
        self.cursor.execute(query)
        # print(cursor.fetchall())
        # exit(1)
        return self.cursor.fetchall()

    # INSERT INTO tbl_name (col1,col2) VALUES(15,col1*2);

    def insert_data(self,table, data):
        # print(data[0][1])
        data[0][1] = "\'" + data[0][1] + "'"
        query = "INSERT INTO {} (".format(table)
        for item in data:
            query += "{} ,".format(item[0])
        query = query.strip(",") + ") VALUES("

        for item in data:
            query += "{},".format(item[1])
        query = query.strip(",") + ");"
        # print(query)
        self.cursor.execute(query)
        self.cnx.commit()

        # a,b,c) VALUES(1,2,3,4,5,6,7,8,9);"



    def queryData(self, queryTable):
        query = "select * from {}".format(queryTable)
        self.cursor.execute(query)
        return self.cursor.fetchall()


if __name__ == '__main__':
    pass
    pass