import datetime
from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.eduBotDB

today = datetime.date.today()
tomorrow = today + datetime.timedelta(days = 1)
tomorrow_day = tomorrow.weekday()
student = db.students.find_one({"phone":"12345678"}, {"class":1})
class_name = student['class']
timetable = db.timetable.find_one({"class":class_name}, {"morning":1, "afternoon":1})
WEEKDAY = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
morning_subjects = timetable['morning'][WEEKDAY[tomorrow_day]]
afternoon_subjects = timetable['afternoon'][WEEKDAY[tomorrow_day]]
print(timetable['afternoon'][WEEKDAY[tomorrow_day]])

message = "Ngày mai không có môn học nào."
if len(morning_subjects) > 0 or len(afternoon_subjects) > 0:
    message = "Sáng mai có các môn: "
    message += " ,".join([subject for subject in morning_subjects])
    message += "\nChiều mai có các môn: "
    message += " ,".join([subject for subject in afternoon_subjects])

print(message)