import os
import sqlite3

#Functions that create tables
dir_of_dir = "carpeta"
dir = "{}\database.db".format(dir_of_dir)

def create_table_student(): #this function try to create a table "students" if this table doesn't exist
    if not os.path.exists(dir_of_dir):
        os.makedirs(dir_of_dir)
    
    sql = sqlite3.connect(dir)
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
        pass
    sql.close()

def create_table_inventory():
    if not os.path.exists(dir_of_dir):
        os.makedirs(dir_of_dir)

    sql = sqlite3.connect(dir)
    try:
        sql.execute('''create table "inventory"(
                        "id_library_item" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                        "author" text,
                        "editorial" text,
                        "category" text,
                        "stock" integer NOT NULL
                    );
        ''')
    except:
        pass
    sql.close()

create_table_student()
create_table_inventory()