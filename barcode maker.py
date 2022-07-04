import os
import qrcode
from datetime import datetime as d
import base64
import sqlite3

def main():
    # User is entering their information.
    navn = input("Navn: ")
    email = input("Email: ")
    date = d.now()

    qr_code = navn + email + str(date)

    # Encoding the data to base64.
    date_bytes = qr_code.encode('ascii')
    base64_bytes = base64.b64encode(date_bytes)

    # Creating a qr code with the data.
    img = qrcode.make(base64_bytes)
    img.save("qr.png", "PNG")

    # Connecting to the database and creating a record with the information
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute("INSERT INTO codetable VALUES (NULL, ?, ?, ?)", (navn, email, base64_bytes))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
