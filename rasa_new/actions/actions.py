# This files contains your custom actions which can be used to run
# custom Python code.

# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests

BASE_URL = "http://worldtimeapi.org/api/timezone"

class ActionHelloWorld(Action):
    """
    Every Class has two methods name & run 

    """

    def name(self) -> Text:
        """
        Returns the name of action

        Returns:
            Text: the text we will register in domain.py

        """
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        

        # we can get values from slots by "tracker objects"

        city = tracker.get_slot('city')
        res = requests.get(BASE_URL+city)
        res = res.json()
        if res['timezone']:
            output = f"Time zone is {res['timezone']}"
        
        else:
            output = "please type in the correct structure: /Area/Region"
        dispatcher.utter_message(text=output)

        return []
