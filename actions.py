# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetSharePrice(Action):

    def name(self) -> Text:
        return "action_get_share_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #use tracker.get_slot to retrieve slot values if they are set
        #foo = tracker.get_slot('your_slot_name')

        #use dispatcher.utter_message to return the message the chatbot should output
        dispatcher.utter_message("Hello World!")

        return []

class ActionGetCeoName(Action):

    def name(self) -> Text:
        return "action_get_ceo_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #use tracker.get_slot to retrieve slot values if they are set
        #foo = tracker.get_slot('your_slot_name')

        #use dispatcher.utter_message to return the message the chatbot should output
        dispatcher.utter_message("I am the CEO :)")

        return []

class ActionGetCeoSal(Action):

    def name(self) -> Text:
        return "action_get_ceo_sal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        #use tracker.get_slot to retrieve slot values if they are set
        #foo = tracker.get_slot('your_slot_name')

        #use dispatcher.utter_message to return the message the chatbot should output
        dispatcher.utter_message("He makes $1 per year")

        return []
