import os

from modules.classes import User, Contact

os.mkdir('user')
os.mkdir('user/dialogs')

New = User()
New.new_user("localhost")
