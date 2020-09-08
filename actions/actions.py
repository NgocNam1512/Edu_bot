from typing import Any, Text, Dict, List
import datetime

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

class ActionGiveScore(Action):
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
        today = datetime.datetime.now().date()
        menu_list = db.menu.find({}, {"date":1, "meal":1})
        foods = []
        message = "Thực đơn hôm nay gồm:\n"
        for menu in menu_list:
            if (menu['date']).date() == today:
                for food in menu['meal']:
                    message += f" - {food}\n"

        dispatcher.utter_message(message)
        return []

class ActionGiveFee(Action):
    def name(self):
        return "action_give_fee"

    def run(self, dispatcher, tracker, domain):
        student_id = tracker.get_slot("phone_number")
        fee = db.fee.find_one({"student_id":student_id}, {"fee":1})
        dispatcher.utter_message(f"Học phí của bạn là {fee['fee']:,}VND")
        
        return []

class ActionGiveAttitude(Action):
    def name(self):
        return "action_give_attitude"

    def run(self, dispatcher, tracker, domain):
        phone_number = tracker.get_slot("phone_number")
        if phone_number is not None:
            today = datetime.datetime.now().date()
            attitude_list = db.attitude.find({"student_id":phone_number}, {"date":1, "attitude":1})
            for attitude in attitude_list:
                if attitude['date'].date() == today:
                    dispatcher.utter_message(f"Nhận xét của giáo viên hôm nay: {attitude['attitude']}")
        else:
            dispatcher.utter_message("Để xem nhận xét của giáo viên bạn cần cung cấp số điện thoại của mình. Số điện thoại của bạn là?")

        return []

class ActionGiveTimetable(Action):
    def name(self):
        return "action_give_timetable"

    def run(self, dispatcher, tracker, domain):
        phone_number = tracker.get_slot("phone_number")
        if phone_number is not None:
            today = datetime.date.today()
            tomorrow = today + datetime.timedelta(days = 1)
            tomorrow_day = tomorrow.weekday()
            student = db.students.find_one({"phone":phone_number}, {"class":1})
            class_name = student['class']
            timetable = db.timetable.find_one({"class":class_name}, {"morning":1, "afternoon":1})
            WEEKDAY = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
            
            morning_subjects = timetable['morning'][WEEKDAY[tomorrow_day]]
            afternoon_subjects = timetable['afternoon'][WEEKDAY[tomorrow_day]]

            message = "Ngày mai không có môn học nào."
            if len(morning_subjects) > 0 and len(afternoon_subjects) > 0:
                message = "Sáng mai có các môn: "
                message += " ,".join([subject for subject in morning_subjects])
                message += "\nChiều mai có các môn: "
                message += " ,".join([subject for subject in afternoon_subjects])

            dispatcher.utter_message(message)
            return []
        else:
            dispatcher.utter_message("Để xem thời khóa biểu bạn cần cung cấp số điện thoại của mình. Số điện thoại của bạn là?")

        return []

class ActionDefaultAskAffirmation(Action):
    """Asks for an affirmation of the intent if NLU threshold is not met."""

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def __init__(self) -> None:
        import pandas as pd

        self.intent_mappings = pd.read_csv("actions/intent_description_mapping.csv")
        self.intent_mappings.fillna("", inplace=True)
        self.intent_mappings.entities = self.intent_mappings.entities.map(
            lambda entities: {e.strip() for e in entities.split(",")}
        )

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        intent_ranking = tracker.latest_message.get("intent_ranking", [])
        if len(intent_ranking) > 1:
            diff_intent_confidence = intent_ranking[0].get(
                "confidence"
            ) - intent_ranking[1].get("confidence")
            if diff_intent_confidence < 0.2:
                intent_ranking = intent_ranking[:2]
            else:
                intent_ranking = intent_ranking[:1]

        # for the intent name used to retrieve the button title, we either use
        # the name of the name of the "main" intent, or if it's an intent that triggers
        # the response selector, we use the full retrieval intent name so that we
        # can distinguish between the different sub intents
        first_intent_names = [
            intent.get("name", "")
            if intent.get("name", "") not in ["out_of_scope"]
            else tracker.latest_message.get("response_selector")
            .get(intent.get("name", ""))
            .get("full_retrieval_intent")
            for intent in intent_ranking
        ]

        message_title = (
            "Sorry, I'm not sure I've understood " "you correctly 🤔 Do you mean..."
        )

        entities = tracker.latest_message.get("entities", [])
        entities = {e["entity"]: e["value"] for e in entities}

        entities_json = json.dumps(entities)

        buttons = []
        for intent in first_intent_names:
            button_title = self.get_button_title(intent, entities)
            if "/" in intent:
                # here we use the button title as the payload as well, because you
                # can't force a response selector sub intent, so we need NLU to parse
                # that correctly
                buttons.append({"title": button_title, "payload": button_title})
            else:
                buttons.append(
                    {"title": button_title, "payload": f"/{intent}{entities_json}"}
                )

        buttons.append({"title": "Something else", "payload": "/trigger_rephrase"})

        dispatcher.utter_message(text=message_title, buttons=buttons)

        return []

    def get_button_title(self, intent: Text, entities: Dict[Text, Text]) -> Text:
        default_utterance_query = self.intent_mappings.intent == intent
        utterance_query = (self.intent_mappings.entities == entities.keys()) & (
            default_utterance_query
        )

        utterances = self.intent_mappings[utterance_query].button.tolist()

        if len(utterances) > 0:
            button_title = utterances[0]
        else:
            utterances = self.intent_mappings[default_utterance_query].button.tolist()
            button_title = utterances[0] if len(utterances) > 0 else intent

        return button_title.format(**entities)

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        # Fallback caused by TwoStageFallbackPolicy
        if (
            len(tracker.events) >= 4
            and tracker.events[-4].get("name") == "action_default_ask_affirmation"
        ):
        #     for event in tracker.events:
        #         print(event.get('name'))
            
        #     dispatcher.utter_message(template="utter_restart_with_button")
            dispatcher.utter_message("Sorry, I will forward your message on to the manager.")

            return []

        # Fallback caused by Core
        else:
            dispatcher.utter_message(template="utter_ask_rephrase")
            return [UserUtteranceReverted()]