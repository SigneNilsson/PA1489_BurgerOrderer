# import the connect method
import mysql.connector
from mysql.connector import connect, errorcode

# define a connection object
#password = 'bestgroupever'
def connect_to_db():
    try:
        conn = connect(
            user = 'root',
            password = '',
            host = 'localhost',
            database = 'menu_store')

        print('A connection object has been created.')
        return conn

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)

    # close the database connection
    conn.close()

