# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted, EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

class StudentForm(FormAction):
    """Collect student info and add to somewhere"""

    def name(self):
        return "student_form"

    @staticmethod
    def required_slots(tracker):
        return [
            "student_name",
            "student_id",
        ]
    
    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
        ) -> List[Dict]:

        dispatcher.utter_message("Cảm ơn cô/ chú đã điền thoong tin")
        # need another action
        return []

class ActionGreetUser(Action):
    """Revertible mapped action for utter_greet"""

    def name(self):
        return "action_greet"
    
    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_greet", tracker)
        return [UserUtteranceReverted()]