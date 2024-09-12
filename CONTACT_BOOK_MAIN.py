import sqlite3

class _Database:
     def create_table():
         conn = sqlite3.connect("Contacts.db")
         cursor = conn.cursor()
     
         cursor.execute(''' CREATE TABLE IF NOT EXISTS Contacts(
                        First_Name TEXT,
                        Last_Name TEXT,
                        Gender TEXT,
                        Ph_Number TEXT PRIMARY KEY,
                        Email TEXT  )''')
         conn.commit()
         conn.close()
     
     def fetch_contacts():
         conn = sqlite3.connect("Contacts.db")
         cursor = conn.cursor()
         cursor.execute("SELECT * FROM CONTACTS")
         contacts = cursor.fetchall()
         conn.close()
         return contacts
     
     def insert_contact(First_Name, Last_Name, Gender, Ph_Number, Email):
         conn = sqlite3.connect("Contacts.db")
         cursor = conn.cursor()
         cursor.execute("INSERT INTO Contacts (First_Name, Last_Name, Gender, Ph_Number, Email) VALUES(?, ?, ?, ?, ?)",(First_Name, Last_Name, Gender, Ph_Number, Email))
         conn.commit()
         conn.close()
     
     def delete_contact(Ph_Number):
         conn = sqlite3.connect("Contacts.db")
         cursor = conn.cursor()
         cursor.execute("DELETE FROM Contacts WHERE Ph_Number = ?",(Ph_Number,))
         conn.commit()
         conn.close()
     
     def update_contact(First_Name, Last_Name, Gender, Ph_Number, Email):
         conn = sqlite3.connect("Contacts.db")
         cursor = conn.cursor()
         cursor.execute("UPDATE Contacts SET First_Name = ?, Last_Name = ?, Gender = ?, Email = ? WHERE Ph_Number = ?",(First_Name, Last_Name, Gender, Email, Ph_Number))
         conn.commit()
         conn.close()
     
     def contact_exists(Ph_Number):
         conn = sqlite3.connect("Contacts.db")
         cursor = conn.cursor()
         cursor.execute("SELECT COUNT(*) FROM Contacts WHERE Ph_Number = ?",(Ph_Number,))
         result = cursor.fetchone()
         conn.close()
         return result[0]>0
     
     def search(Ph_Number):
        conn = sqlite3.connect("Contacts.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Contacts WHERE Ph_Number = ?", (Ph_Number,))
        return cursor.fetchone()

     create_table()