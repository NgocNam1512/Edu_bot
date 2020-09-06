from typing import Any, Text, Dict, List
from datetime import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.events import (
    UserUtteranceReverted,
    EventType,
    SlotSet,
)
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.eduBotDB

class PhoneNumberForm(FormAction):
    def name(self):
        return "phone_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "phone_number",
        ]
    
    def slot_mappings(self):
        return {
            "phone_number": [
                self.from_text(),
            ]
        }
    
    def validate_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        phone = db.students.find_one({"phone":value})
        if phone is None:
            dispatcher.utter_message("Invalid phone number. Please try again.")
            return {"phone_number": None}
        return {"phone_number": value}
    
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        dispatcher.utter_message("Số điện thoại đã được ghi nhận. Bạn cần tôi giúp gì?")
        return []

class ActionGiveDailyScore(Action):
    def name(self):
        return "action_give_score"

    def run(self, dispatcher, tracker, domain):
        phone_number = tracker.get_slot("phone_number")
        if phone_number is not None:
            if (tracker.get_slot("mid_score") is not None):
                if (tracker.get_slot("subject") is not None):
                    subject = tracker.get_slot("subject").capitalize()
                    score = db.midScore.find_one({"subject":subject, "student_id":phone_number},{"_id":0, "score":1})
                    message = f"Điểm {subject} giữa kỳ là {score['score']}"
                    dispatcher.utter_message(message)
                    return [SlotSet("subject", None), SlotSet("mid_score", None)]
                
                scores = db.midScore.find({"student_id":phone_number},{"subject":1, "score":1})
                message = "Điểm giữa kỳ:\n"
                for score in scores:
                    message += f"Môn {score['subject']}: {score['score']}\n"
                dispatcher.utter_message(message)
                return [SlotSet("mid_score", None)]

            elif (tracker.get_slot("end_score") is not None):
                if (tracker.get_slot("subject") is not None):
                    subject = tracker.get_slot("subject").capitalize()
                    score = db.endScore.find_one({"subject":subject, "student_id":phone_number},{"_id":0, "score":1})
                    message = f"Điểm {subject} cuối kỳ là {score['score']}"
                    dispatcher.utter_message(message)
                    return [SlotSet("subject", None), SlotSet("end_score", None)]
                
                scores = db.endScore.find({"student_id":phone_number},{"subject":1, "score":1})
                message = "Điểm cuối kỳ:\n"
                for score in scores:
                    message += f"Môn {score['subject']}: {score['score']}\n"
                dispatcher.utter_message(message)
                return [SlotSet("end_score", None)]

            ## if daily_score
            if (tracker.get_slot("subject") is not None):
                subject = tracker.get_slot("subject").capitalize()
                score = db.dailyScore.find_one({"subject":subject, "student_id":phone_number},{"_id":0, "score":1})
                message = f"Điểm {subject} hôm nay là {score['score']}"
                dispatcher.utter_message(message)
                return [SlotSet("subject", None), SlotSet("daily_score", None)]
            
            scores = db.dailyScore.find({"student_id":phone_number},{"subject":1, "score":1})
            message = "Điểm miệng hôm nay:\n"
            for score in scores:
                message += f"Môn {score['subject']}: {score['score']}\n"
            dispatcher.utter_message(message)
            return [SlotSet("daily_score", None)]
        else:
            dispatcher.utter_message("Để tra cứu điểm bạn cần cung cấp số điện thoại của mình. Số điện thoại của bạn là?")
        return []

class ActionGiveMenu(Action):
    def name(self):
        return "action_give_menu"

    def run(self, dispatcher, tracker, domain):
        today = datetime.now().date()
        menu_list = db.menu.find({}, {"date":1, "meal":1})
        foods = []
        message = "Thực đơn hôm nay gồm:\n"
        for menu in menu_list:
            if (menu['date']).date() == today:
                for food in menu['meal']:
                    message += f" - {food}\n"

        dispatcher.utter_message(message)
        return []

class ActionGiveAttitude(Action):
    def name(self):
        return "action_give_attitude"

    def run(self, dispatcher, tracker, domain):
        phone_number = tracker.get_slot("phone_number")
        if phone_number is not None:
            today = datetime.now().date()
            attitude_list = db.attitude.find({"student_id":phone_number}, {"date":1, "attitude":1})
            for attitude in attitude_list:
                if attitude['date'].date() == today:
                    dispatcher.utter_message(f"Nhận xét của giáo viên hôm nay: {attitude['attitude']}")
        else:
            dispatcher.utter_message("Để xem nhận xét của giáo viên bạn cần cung cấp số điện thoại của mình. Số điện thoại của bạn là?")

        return []