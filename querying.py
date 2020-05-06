import sqlite3

connection = sqlite3.connect('chinook.db')

# cursors allow us to interact with the database
cursor = connection.cursor()

# executing a select
result_set = cursor.execute('SELECT * FROM Track')
for row in result_set:
    # index columns by integer index
    print(row)

# indexing by column name
connection.row_factory = sqlite3.Row
result_set = cursor.execute('SELECT * FROM Track')
for row in result_set:
    # index columns by column name
    print(row)

# arguments must be a tuple, even if there's only one
favorite_artist = ('Miles Davis',)
result_set = cursor.execute('SELECT * FROM Track WHERE Composer=?', favorite_artist)
# always do this; NEVER use Python's format or % because of SQL injection attacks

# get one at a time
print(result_set.fetchone())
print(result_set.fetchone())

# make sure you close the cursor and the database connection!
cursor.close()
# after this point, we can't use "cursor" anymore; must request a new cursor from the connection
connection.close()
