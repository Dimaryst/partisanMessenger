import hashlib
import json
import os
import sqlite3
from datetime import datetime


class User:
    def __init__(self):
        self.uuid = None
        self.ip = None
        self.port = 41030  # Default Port

    def new_user(self, ip=str, entropy="entropy"):
        uuid = hashlib.sha256()
        uuid.update(str(datetime.now()).encode('utf-8'))
        uuid.update(ip.encode('utf-8'))
        uuid.update(entropy.encode('utf-8'))
        self.uuid = uuid.hexdigest()
        self.ip = ip
        self.new_card()
        self.new_database()

    def new_database(self):
        conn = sqlite3.connect(f"user/{self.uuid}.db")
        cur = conn.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS contacts(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               nickname TEXT,
               uuid TEXT,
               duid TEXT,
               ip TEXT,
               port INT,
               interval INT, 
               is_paired INT,
               is_available INT);
            """)
        self_as_contact = (0, 'SELF', self.uuid, "0", self.ip, self.port, 0, 1, 1)
        cur.execute(f"""INSERT INTO
            contacts(id, nickname, uuid, duid, ip, port, interval, is_paired, is_available)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);""", self_as_contact)
        conn.commit()
        conn.close()

        conn = sqlite3.connect(f"user/dialogs/dialog{self.uuid}.db")
        cur = conn.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS messages(
                      id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
                      message TEXT,
                      hash TEXT,
                      date TEXT,
                      status TEXT);
                   """)
        row = (0, 'START', "START", str(datetime.now()).encode('utf-8'), "START_MESSAGE")
        cur.execute(f"""INSERT INTO
                   messages(id, message, hash, date, status)
                   VALUES(?, ?, ?, ?, ?);""", row)
        conn.commit()
        conn.close()

    def new_card(self):
        card = {
            'UUID': self.uuid,
            'IP': self.ip,
            'PORT': self.port
        }
        with open(f"user/{self.uuid}.json", "w") as card_file:
            json.dump(card, card_file, indent=4)

    def get_contacts(self):
        conn = sqlite3.connect(f"user/{self.uuid}.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contacts;")
        result = cur.fetchall()
        conn.close()
        return result


class Contact:
    def __init__(self, user):
        self.contacts_db_path = f"user/{user.uuid}.db"
        self.contact_nickname = None
        self.contact_uuid = None
        self.contact_duid = "0"
        self.contact_ip = None
        self.contact_port = 41030
        self.contact_interval = 0
        self.contact_is_paired = 0
        self.contact_is_available = 0

    def add_contact(self):
        conn = sqlite3.connect(self.contacts_db_path)
        cur = conn.cursor()
        new_contact = (self.contact_nickname, self.contact_uuid,
                       self.contact_duid, self.contact_ip, self.contact_port,
                       0, 0, 0)
        cur.execute(f"""INSERT INTO
            contacts(nickname, uuid, duid, ip, port, interval, is_paired, is_available)
            VALUES(?, ?, ?, ?, ?, ?, ?, ?);""", new_contact)
        conn.commit()
        conn.close()
        self.new_database()

    def remove_contact(self, cuuid):
        conn = sqlite3.connect(self.contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM contacts WHERE uuid = \'{cuuid}\';")
        conn.commit()
        conn.close()
        if os.path.exists(f'user/dialogs/dialog{cuuid}.db'):
            os.remove(f'user/dialogs/dialog{cuuid}.db')

    def existing_contact(self, cuuid):
        conn = sqlite3.connect(self.contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE uuid = \'{cuuid}\';")
        request_result = cur.fetchone()
        self.contact_nickname = request_result[1]
        self.contact_uuid = request_result[2]
        self.contact_duid = request_result[3]
        self.contact_ip = request_result[4]
        self.contact_port = request_result[5]
        self.contact_interval = request_result[6]
        self.contact_is_paired = request_result[7]
        self.contact_is_available = request_result[8]
        conn.close()

    def contact_info(self):
        return (self.contact_nickname, self.contact_uuid,
                self.contact_duid, self.contact_ip, self.contact_port,
                self.contact_interval, self.contact_is_paired, self.contact_is_available)

    def new_database(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.contact_uuid}.db")
        cur = conn.cursor()
        cur.execute(f"""CREATE TABLE IF NOT EXISTS messages(
               id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, 
               message TEXT,
               hash TEXT,
               date TEXT,
               status TEXT);
            """)
        row = (0, 'START', "START", str(datetime.now()).encode('utf-8'), "START_MESSAGE")
        cur.execute(f"""INSERT INTO
            messages(id, message, hash, date, status)
            VALUES(?, ?, ?, ?, ?);""", row)
        conn.commit()
        conn.close()

    def get_messages(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.contact_uuid}.db")
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM messages;")
        result = cur.fetchall()
        conn.close()
        return result


class Message:
    def __init__(self, contact):
        if contact is None:
            self.to_contact = None
        else:
            self.to_contact = contact

        self.message = None
        self.hash = None  # not using
        self.date = str(datetime.now())
        self.status = None  # # not using

    def save(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.to_contact.contact_uuid}.db")
        cur = conn.cursor()
        row = (self.message, 'hash', self.date, 'SENT')
        cur.execute(f"""INSERT INTO
            messages(message, hash, date, status)
            VALUES(?, ?, ?, ?);""", row)
        conn.commit()
        conn.close()

    def send(self):
        # TODO: Func for messages
        print(f"\'{self.message}\' ({self.date})")
        print("Will send to " + self.to_contact.contact_nickname)
        print("At " + self.to_contact.contact_ip)
        package = (self.to_contact.contact_uuid, self.message, self.date)
        print("DATA: ", package)

    def add_hash(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.to_contact.contact_uuid}.db")
        cur = conn.cursor()
        cur.execute("SELECT hash from messages WHERE id=(SELECT max(id) FROM messages);")
        result = cur.fetchone()
        hs = hashlib.sha256()
        # hs.update()
