"""Using Pyhthon's sqlite3 library to connect to an SQLite database
SQLite is probably the most straightforward database to connect to with a Python application since 
you don’t need to install any external Python SQL modules to do so. By default, your Python 
installation contains a Python SQL library named sqlite3 that you can use to interact with an SQLite 
database
What’s more, SQLite databases are serverless and self-contained, since they read and write data to a 
file. This means that, unlike with MySQL and PostgreSQL, you don’t even need to install and run an 
SQLite server to perform database operations!
Reference: https://realpython.com/python-sql-libraries/
"""

import sqlite3

from sqlite3 import Error


def create_connection(path):
    """If the database exists at the specified location, then a connection to the database is established\
    Otherwise, a new database is created at the specified location, and a connection is established."""
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error {e} occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print("The error '" + str(e) + "' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print("The error '" + str(e) + "' occurred")
#the .fetchall() method returns a list of tuples where each tuple is 
# mapped to the corresponding row in the retrieved records

path = "C:\\users\\student\\repo2020\\my_app.sqlite"
connection = create_connection(path)

create_users_table = """CREATE TABLE IF NOT EXISTS users (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        name TEXT NOT NULL,
                                        age INTEGER,
                                        gender TEXT,
                                        nationality TEXT
                                    ); """

create_posts_table = """CREATE TABLE IF NOT EXISTS posts(
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        title TEXT NOT NULL,
                                        description TEXT NOT NULL,
                                        user_id INTEGER NOT NULL,
                                        FOREIGN KEY (user_id)
                                        REFERENCES users (id)
                                    ); """
                                 
create_comments_table = """CREATE TABLE IF NOT EXISTS comments (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        text TEXT NOT NULL,
                                        user_id INTEGER NOT NULL,
                                        post_id INTEGER NOT NULL,
                                        FOREIGN KEY (user_id)
                                        REFERENCES users (id)
                                        FOREIGN KEY (post_id)
                                        REFERENCES posts (id)
                                    ); """

create_likes_table = """CREATE TABLE IF NOT EXISTS likes (
                                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                                        user_id INTEGER NOT NULL,
                                        post_id integer NOT NULL,
                                        FOREIGN KEY (user_id)
                                        REFERENCES users (id)
                                        FOREIGN KEY (post_id)
                                        REFERENCES posts (id)
                                    ); """

#we now create four tables
execute_query(connection, create_users_table)
execute_query(connection, create_posts_table)
execute_query(connection, create_comments_table)  
execute_query(connection, create_likes_table)

#and now we add records
create_users = """ INSERT INTO users (name, age, gender, nationality)
                   VALUES ('James', 25, 'male', 'USA'),
                   ('Leila', 32, 'female', 'France'),
                   ('Brigitte', 35, 'female', 'England'),
                   ('Mike', 40, 'male', 'Denmark'),
                   ('Elizabeth', 21, 'female', 'Canada');"""
#Since you set the id column to auto-increment, you don’t need to 
# specify the value of the id column for these users. The users 
# table will auto-populate these five records with id values from 1 to 5

create_posts = """ INSERT INTO posts (title, description, user_id)
                   VALUES ('Happy', 'I am feeling very happy today', 1),
                   ('Hot Weather', 'The weather is very hot today', 2),
                   ('Help', 'I need some help with my work', 2),
                   ('Great News', 'I am getting married', 1),
                   ('Interesting Game', 'It was a fantastic game of tennis', 5),
                   ('Party', 'Anyone up for a late night party today?', 3);"""
#It’s important to mention that the user_id column of the posts table is a 
# foreign key that references the id column of the users table. This means that 
# the user_id column must contain a value that already exists in the id column 
# of the users table. If it doesn’t exist, then you’ll see an error.

create_comments = """ INSERT INTO comments (text, user_id, post_id)
                   VALUES ('Count me in', 1, 6),
                   ('What sort of help?', 5, 3),
                   ('Congrats buddy', 2, 4),
                   ('I was rooting for Nadal though', 4, 5),
                   ('Help with your thesis?', 2, 3),
                   ('Many congratulations', 5, 4);"""

create_likes = """ INSERT INTO likes (user_id, post_id)
                   VALUES (1, 6),
                   (2, 3),
                   (1, 5),
                   (5, 4),
                   (2, 4),
                   (4, 2),
                   (3, 6);"""

execute_query(connection, create_users)
execute_query(connection, create_posts)          
execute_query(connection, create_comments)
execute_query(connection, create_likes) 

#we now select/retrieve all records from the users table
select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

#retrieve all records from the posts table (which is joined to
# the users table via a posts.foreign_key = users.primary_key)
select_users_posts = """SELECT users.id, users.name, posts.description
                 FROM posts
                 INNER JOIN users ON users.id = posts.user_id"""
users_posts = execute_read_query(connection, select_users_posts)
for users_post in users_posts:
    print(users_post)

#You can also select data from three related tables by implementing multiple 
# JOIN operators. The following script returns all posts, along with the 
# comments on the posts and the names of the users who posted the comments:
select_posts_comments_users = """SELECT posts.description as post,
                                 text as comment, name
                                 FROM posts
                                 INNER JOIN comments
                                 ON
                                 posts.id = comments.post_id
                                 INNER JOIN users
                                 ON
                                 users.id = comments.user_id"""
posts_comments_users = execute_read_query(connection,
                                          select_posts_comments_users)
for posts_comments_user in posts_comments_users:
    print(posts_comments_user)
