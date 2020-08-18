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

from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.test

class TestMogoDB(Action):
    """Test mongo db"""
    def name(self):
        return "action_test_mongodb"

    def run(self, dispatcher, tracker, domain):
        #db.inventory.insert({"name":"rasa"})
        results = db.inventory.find({"status":"D"}, {"_id":0, "item":1})
        for result in results:
            print(result['item'])
        dispatcher.utter_message("Inserted to mongodb")
        return[]