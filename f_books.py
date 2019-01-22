# -*- coding: utf-8 -*-

from flask import Flask, request, render_template, url_for, redirect, session, flash, g
import os
import sqlite3

def create_db():
    with sqlite3.connect(r"C:\Users\qli1\BNS_wspace\flask\f_books\books.db") as connection:
        conn = connection.cursor()
        conn.execute("CREATE TABLE IF NOT EXISTS books(author TEXT, title TEXT, genre TEXT, price REAL)")
        books_data = [
                ("Steven King", "IT", "Horror", 7.99),
                ("Dan Brown", "The Davinci Code", "Thriller", 8.99),
                ("Alexander Dumas", "The Count of Monte Cristo", "Adventure", 10.99),
                ("James H. Chase", "Shogun", "Action", 3.55)
            ]
        conn.executemany("INSERT INTO books VALUES(?, ?, ?, ?)", books_data)
        
        conn.execute("SELECT * FROM books")
        data = conn.fetchone()
        conn.close()
        print(data)



# for c9 users
host = os.getenv("IP", "127.0.0.1")
port = int(os.getenv("PORT", "8080"))

# configuration details
DATABASE = "C:\\Users\qli1\BNS_wspace\flask\f_books\books.db"
SECRET_KEY = "my_secret"

app = Flask(__name__)
app.config.from_object(__name__) # pulls in app configuration by looking for uppercase variables

# create function to connect to database
def connect_db():
#    return sqlite3.connect(app.config["C:\Users\qli1\BNS_wspace\flask\f_books\books.db"])
    connect=sqlite3.connect(r"C:\Users\qli1\BNS_wspace\flask\f_books\books.db")
    return connect
    
    
# create views/routes
#@app.route("/")
#def login():
#    return render_template("login.html")
    
    
@app.route("/main")
def main():
    # create connection to db
    g.db = connect_db()
    # create a cursor to db
    conn = g.db.cursor()
    # execute a query against db
    conn.execute("SELECT * FROM books")
    books_data = conn.fetchall()
    
    # how do we want to display the data? In a list
    books = []
    # books data is a list of records that have same column items
    # i.e author, title, genre, price, best represented in a dictionary
    # iterate over books data and populate books list with data
    for book in books_data:
        books.append({"id":book[0], "author":book[1], "title":book[2], "genre":book[3], "price":book[4]})
        
    # close db connection
    g.db.close()
    # pass books data to our template for use
    return render_template("main.html", books=books)

# edit route
@app.route("/edit", methods=["GET", "POST"])
def edit():
    
    msg = ""
    
    # get query string arguments
    book_id = request.args.get("book_id")
    author = request.args.get("author")
    title = request.args.get("title")
    genre = request.args.get("genre")
    price = request.args.get("price")
    
    book = {
        "book_id": book_id,
        "author":author,
        "title":title,
        "genre":genre,
        "price":price
    }
    
    if request.method == "POST":
        # get the data from form
        book_id = request.form["book_id"]
        author = request.form["author"]
        title = request.form["title"]
        genre = request.form["genre"]
        price = request.form["price"]
        
        # connect db and update record
        g.conn = connect_db()
        cursor = g.conn.cursor()
        cursor.execute("UPDATE books SET author=?, title=?, genre=?, price=? WHERE id=?", (author, title, genre, price, trd_id))
        
        g.conn.commit()
        g.conn.close()
        
        book = {
            "book_id": book_id,
            "author":author,
            "title":title,
            "genre":genre,
            "price":price
        }
        
        msg = "Record successfully updated!"
    
    return render_template('edit.html', book_record=book, message=msg)
    
if __name__ == "__main__":
    app.run(host=host, port=port, debug=True)
        