import os
import sqlite3

class Create:
    """That class create functions which create tables"""
    folder = "carpeta_2"
    database_name = "{}\database.db".format(folder)

    def create_table_student(self): 
        """this function try to create a table "students" if this table doesn't already exist"""
        try:
            os.makedirs(self.folder)
            print("carpeta creada")
        except:
            pass
        
        sql = sqlite3.connect(self.database_name)
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

    def create_table_inventory(self): 
        """this function try to create a table "inventory" if this table doesn't already exist"""
        try:
            os.makedirs(self.folder)
            print("carpeta creada")
        except:
            pass

        sql = sqlite3.connect(self.database_name)
        try:
            sql.execute('''create table "inventory"(
                            "id_library_item" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                            "author" text,
                            "editorial" text,
                            "category" text,
                            "stock" integer NOT NULL,
                            "item" text NOT NULL
                        );
            ''')
        except:
            pass
        sql.close()

    def create_table_borrowed(self): 
        """this function try to create a table of the relation of the tables "students" and "inventory" if this table doesn't already exist"""

        try:
            os.makedirs(self.folder)
            print("carpeta creada")
        except:
            pass

        sql = sqlite3.connect(self.database_name)
        try:
            sql.execute("""CREATE TABLE 'borrowed' (
                            'id_library_item_borrowed'	INTEGER,
                            'dni_student_borrowed'	INTEGER,
                            'date_out'	DATE,
                            'date_in'	DATE,
                            FOREIGN KEY('id_library_item_borrowed') REFERENCES 'inventory'('id_library_item'),
                            FOREIGN KEY('dni_student_borrowed') REFERENCES 'student'('dni_student')
                        );
            """)
        except:
            pass
        sql.close()

