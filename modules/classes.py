import hashlib
import json
import os
import socket
import sqlite3
from datetime import datetime


class User:
    def __init__(self):
        self.__name = 'self'
        self.uuid = None
        self.ip = None
        self.port = 7045  # Default Port

    def new_user(self, ip=str, entropy="entropy"):
        uuid = hashlib.sha1()
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
        self_as_contact = (0, 'self', self.uuid, "0", self.ip, self.port, 0, 1, 1)
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

    def set_name(self, name):
        self.__name = name


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
        cur.execute(f"SELECT * FROM messages WHERE id > 0;")
        result = cur.fetchall()
        conn.close()
        return result

    def delete_messages(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.contact_uuid}.db")
        cur = conn.cursor()
        cur.execute("DELETE FROM messages WHERE id > 0;")
        conn.commit()
        conn.close()

    def last_message_id(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.contact_uuid}.db")
        cur = conn.cursor()
        cur.execute(f"SELECT id FROM messages WHERE id=(SELECT max(id) FROM messages);")
        result = cur.fetchone()
        conn.close()
        return result

    def is_exist(self, cuuid=None):
        conn = sqlite3.connect(self.contacts_db_path)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM contacts WHERE uuid = \'{cuuid}\';")
        request_result = cur.fetchone()
        if request_result != '':
            return True
        else:
            return False


class Message:
    def __init__(self, contact, sender):
        self.to_contact = contact
        self.sender = sender
        self.message, self.status = None, None
        self.hash = "hash"
        self.date = str(datetime.now())

    def load(self, package):
        self.message = package[2]
        self.hash = package[3]

    def save(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.to_contact.contact_uuid}.db")
        cur = conn.cursor()
        row = (f"(ME) > \n{self.message}", self.hash, self.date, 'STATUS')
        cur.execute(f"""INSERT INTO
            messages(message, hash, date, status)
            VALUES(?, ?, ?, ?);""", row)
        conn.commit()
        conn.close()

    def send(self):
        package = (self.sender.uuid, self.to_contact.contact_uuid, self.message, self.date)
        package = json.dumps(package)
        print("Trying to send to recipient: ", self.to_contact.contact_ip, self.to_contact.contact_port)
        print(package)

        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        try:
            sock.connect((self.to_contact.contact_ip, self.to_contact.contact_port))
            print("Trying to send to recipient: ", self.to_contact.contact_ip, socket.SOCK_STREAM)
            print(package)
            sock.send(str(package).encode('utf-8'))

        except Exception as e:
            print(f"Failed ({e})")
        finally:
            sock.close()

    def add_hash(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.to_contact.contact_uuid}.db")
        cur = conn.cursor()
        cur.execute("SELECT hash from messages WHERE id=(SELECT max(id) FROM messages);")
        result = cur.fetchone()
        hs = hashlib.sha256(str(result).encode('utf-8'))
        hs.update(self.message.encode('utf-8'))
        self.hash = hs.hexdigest()

    def receive(self):
        conn = sqlite3.connect(f"user/dialogs/dialog{self.sender.contact_uuid}.db")
        cur = conn.cursor()
        row = (f"({self.sender.contact_uuid}) > \n{self.message}", self.hash, self.date, 'STATUS')
        cur.execute(f"""INSERT INTO
                    messages(message, hash, date, status)
                    VALUES(?, ?, ?, ?);""", row)
        conn.commit()
        conn.close()
