import sqlite3
from datetime import datetime


class Profile:
    def __init__(self, ip):
        self.__ip = ip

    def new_contact_list(self):
        self_as_contact = (0, self.__ip, "Me")
        database_name = self.__ip.replace(":", "")
        conn = sqlite3.connect(f"profile/{database_name}.db")
        cur = conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               ip TEXT,
               name TEXT);""")
        cur.execute("INSERT INTO contacts(id,ip,name)"
                    "VALUES(?, ?, ?);", self_as_contact)
        conn.commit()
        conn.close()

    def get_contacts(self):
        conn = sqlite3.connect(f"profile/{self.__ip}.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contacts;")
        result = cur.fetchall()
        conn.close()
        return result

    def get_profile_ip(self):
        return self.__ip


class Contact:
    def __init__(self, profile):
        self.profile = profile
        self.__ip = None
        self.__name = None
        self.__contacts_db_path = f"user/contacts.db"

    def set_ip(self, ip):
        self.__ip = ip

    def set_name(self, name):
        self.__name = name

    def load_existing_contact(self, contact_name):
        conn = sqlite3.connect(self.__contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE name = \'{contact_name}\';")
        request_result = cur.fetchone()
        self.__ip = request_result[1]
        self.__name = request_result[2]
        conn.close()

    def add_new_contact(self):
        conn = sqlite3.connect(self.__contacts_db_path)
        cur = conn.cursor()
        new_contact = (self.__ip, self.__name)
        cur.execute(f"""INSERT INTO
            contacts(ip, name)
            VALUES(?, ?);""", new_contact)
        conn.commit()
        conn.close()

    def edit_contact(self, new_contact_name, new_contact_ip):
        conn = sqlite3.connect(self.__contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"UPDATE contacts SET name = \'{new_contact_name}\', ip = \'{new_contact_ip}\' "
                    f"WHERE name = \'{self.__name}\';")
        conn.commit()
        conn.close()

    def remove_contact(self, contact_name):
        conn = sqlite3.connect(self.__contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM contacts WHERE name = \'{contact_name}\';")
        conn.commit()
        conn.close()

    def is_exist(self, contact_name):
        conn = sqlite3.connect(self.__contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE name = \'{contact_name}\';")
        request_result = cur.fetchone()
        if request_result != '':
            return True
        else:
            return False

