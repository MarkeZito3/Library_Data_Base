import os
import sqlite3

def create_table_student(): #this function try to create a table "students" if this table doesn't exist
    if not os.path.exists("Library_Data_Base\dependences\carpeta"):
        os.makedirs("Library_Data_Base\dependences\carpeta")
    
    sql = sqlite3.connect("Library_Data_Base\dependences\carpeta\database.db")
    try:
        sql.execute('''CREATE TABLE "student" (
                    "dni_student" INTEGER NOT NULL UNIQUE,
                    "name" TEXT NOT NULL,
                    "surname" TEXT NOT NULL,
                    "phone" INTEGER NOT NULL,
                    "email" text NOT NULL,
                    "classroom" text NOT NULL,
                    "gender" text NOT NULL,
                    "address" text NOT NULL,
                    "birthday" DATE NOT NULL,
                    "borrowed_library_items" INTEGER,
                    PRIMARY KEY ("DNI_student")
                );''')
    except:
        print("carpeta creada")
    sql.close()

"""def create_table_inventory():
    sql = sqlite3.connect("Library_Data_Base\dependences\database.db")"""

create_table_student()