import sqlite3

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = "SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"

    cursor.execute(query)
    user = cursor.fetchone()

    if user:
        print("Login successful!")
    else:
        print("Invalid username or password.")

    conn.close()


username = input("Enter username: ")
password = input("Enter password: ")

login(username, password)
