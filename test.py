import datetime
from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.eduBotDB

date = datetime.date.today()
tomorrow = date + datetime.timedelta(days = 1)

# student = db.students.find_one({"phone":"12345678"}, {"class":1})
# print(str(date)+"T00:00:00.000Z")

# today = str(date)+"T00:00:00.000Z"
# tomorrow = str(tomorrow)+"T00:00:00.000Z"

# date = db.menu.find_one({"date": date}, {"date":1})
# date = datetime.datetime(2020, int(month), int(day)).isoformat()
# print(date)
# {"$gte":date.isoformat(),  
#                                 "$lt":(date + datetime.timedelta(days = 1)).isoformat()}

def time_preprocess(time):
    if time == "ngày mai":
        date = datetime.date.today() + datetime.timedelta(days = 1)
    elif time == "hôm qua":
        date = datetime.date.today() - datetime.timedelta(days = 1)
    elif time == "hôm nay":
        date = datetime.date.today()
    else:
        for c in ['-', '/', '.']:
            if c in time:
                time_arr = time.split(c)
        (day, month) = time_arr[:2]
        date = datetime.date(2020, int(month), int(day))
    return date

date = time_preprocess("8-9-2020")
menu = db.menu.find_one({"date":date})
print(menu)