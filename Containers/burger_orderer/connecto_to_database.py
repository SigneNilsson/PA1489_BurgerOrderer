# import the connect method
from mysql.connector import connect

# define a connection object
conn = connect(
    user = 'root',
    password = 'bestgroupever',
    host = 'localhost',
    database = 'menu_store')

print('A connection object has been created.')

# close the database connection
conn.close()
