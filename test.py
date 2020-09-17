import datetime
from pymongo import MongoClient
import dns

client = MongoClient('mongodb+srv://admin:admin-password@cluster0.cgpcq.mongodb.net/eduBot')
db = client.eduBot

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

# today = datetime.date.today()
# print(today)
# tomorrow = today + datetime.timedelta(days = 1)
# print(tomorrow)
# print(type(tomorrow))
# tomorrow_day = tomorrow.weekday()
# print(tomorrow_day)

time = "15/06"
date = time_preprocess(time)
week_day = date.weekday()
student = db.students.find_one({"phone":"0326882683"}, {"class":1})
class_name = student['class']
timetable = db.timetable.find_one({"class":class_name}, {"morning":1, "afternoon":1})
WEEKDAY = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
print(week_day)