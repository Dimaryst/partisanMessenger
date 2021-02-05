import os

from modules.classes import User, Contact

os.mkdir('user')
os.mkdir('user/dialogs')

New = User()
New.new_user("200:5011:1b47:3a14:6322:c4c7:c24d:eff4")
