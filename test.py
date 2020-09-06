from datetime import datetime
from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.eduBotDB

now = datetime.now().date()
print(now)

menu_list = db.menu.find({}, {"date":1, "meal":1})
for menu in menu_list:
    if (menu['date'].date() == now):
        print(menu['meal'])

