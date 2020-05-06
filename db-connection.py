# sqlite3 – the Python library we will be using to connect to the database.
import sqlite3

# open a database connection
connection = sqlite3.connect('chinook.db')

# ask the connection for a cursor object
# the cursor object is used to interact with the DB and execute queries
cursor = connection.cursor()

# run a query
# this is vulnerable to SQL Injection attack
# result_set = cursor.execute('SELECT * FROM Track')

# select all rows where composer is Miles Davis
# use the cursor object to sanitize the input to prevent an attack
# must be specified in tuple, thats what the extra comma indicates
favorite_artist = ('Miles Davis',)

#result_set = cursor.execute('SELECT * FROM Track WHERE Composer = "Miles Davis"')
result_set = cursor.execute('SELECT * FROM Track WHERE Composer = ?', favorite_artist)

# print a single row at a time
# note this prints first 2 rows in result set and then loop continues at 3rd row
print('# ---------------------------------- #')
print(result_set.fetchone())
print(result_set.fetchone())
print('# ---------------------------------- #')

#cursor will execute the query and store results in the result set
# row = tuple object where each element is a value
for row in result_set:
    print (row)       # prints all columns in all rows
    # print (row[1])      # prints only first column in each row

# close the cursor
# once closed, a cursor object cannot be used again. We have to get a new cursor from the connection
cursor.close() 

# close the database connection
# this is to tell the database that we are done working with it and it can release any memory and resources associated with this connection.
connection.close() 
