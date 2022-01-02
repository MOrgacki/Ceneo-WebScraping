import sqlite3
from sqlite3 import Error


class DataBaseHandler:

    def __init__(self):
            database = r"/home/organ/Desktop/WebScraping/Ceneo-WebScraping/Data.db"

            sql_create_offers_table = """ CREATE TABLE IF NOT EXISTS offers (
                                                id varchar(500) PRIMARY KEY,
                                                logo text,
                                                price integer,
                                                actual date
                                            ); """

            # create a database connection
            self.conn = self.create_connection(database)

            # create tables
            if self.conn is not None:
                # create offers table
                self.create_table(self.conn, sql_create_offers_table)
            else:
                print("Error! cannot create the database connection.")
    
    @classmethod
    def create_connection(cls, db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return conn
        
    @classmethod
    def create_table(cls, conn, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

    def create_offer(self, conn, offer):
        """
        Create a new offer into the offers table
        :param conn:
        :param logo:
        :param price:
        :param actual:
        :return: offer id
        """
        sql = ''' INSERT INTO offers(id,logo,price,actual)
                VALUES(?,?,?,?) '''
        cur = conn.cursor()
        cur.execute(sql, offer)
        conn.commit()
        return cur.lastrowid

    
    def filter_best_offer(self, conn):
        """ return the best offer today"""
        sql = ''' SELECT MIN(price),logo,id
        FROM offers; '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        rows = cur.fetchall()
        
        return rows