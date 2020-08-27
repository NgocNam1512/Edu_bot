from typing import Any, Text, Dict, List
import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.events import (
    UserUtteranceReverted,
    EventType,
    ReminderCancelled,
    ReminderScheduled,
    SlotSet,
)
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.eduBotDB

class ActionGiveDailyScore(Action):
    def name(self):
        return "action_give_score"

    def run(self, dispatcher, tracker, domain):
        phone_number = tracker.get_slot("phone_number")
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