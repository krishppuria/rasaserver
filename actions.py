from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class Actioneligibility(Action):
  def name(self):
    return 'action_eligibility'

  def run(self, dispatcher, tracker, domain):
    loc=tracker.get_slot('course')
    dic={"btech":"10+2 with minimum 50% (45% for “SC/ST/OBC/SBC) marks from CBSE/equivalent\
                  board along with 45% (40% for ST/SC/OBC/SBC) marks in Mathematics and Physics\
                  and any one of Chemistry/Computer Science/IP/Biology/Bio-technology.",
        "mtech":"BE/ BTech/ equivalent in relevant discipline from a recognized\
                  university with 55% marks or 6.25 CGPA on 10 points scale (50% or 5.75\
                  CGPA on 10 points scale for ST/SC/OBC/SBC).Candidates with MCA/MSc IT also\
                  considered.",
        "msc":"10+2 (PCM) with 50% marks (45% for SC/ST/OBC/SBC) from CBSE/equivalent board.",
        "barch":"10 + 2 With Maths (50 % Aggregate) from CBSE/equivalent board + valid NATA Score\
                  as per NATA 2018 guidelines or valid JEE paper 2 score.",
        "bca":"10+2 (any stream) of CBSE / equivalent board."
    }
    dispatcher.utter_message(dic[loc])
    return []

class Actionfee(Action):
  def name(self):
    return 'action_fee'

  def run(self, dispatcher, tracker, domain):
    loc=tracker.get_slot('course')
    dic={"btech":"1.5lac",
        "mtech":"2.55lac",
        "msc":"1lac",
        "bca":"0.6lac"
    }
    dispatcher.utter_message(dic[loc])
    return []

