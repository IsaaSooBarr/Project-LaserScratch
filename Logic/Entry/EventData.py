from Utility.ByteStream import Writer
from Utility.Utils import Utils


class EventSlots:
    EventsData = [
        {
            'EventIndex': 1,
            'NewEventReward': 10,
            'LocationID': 7,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 2,
            'NewEventReward': 10,
            'LocationID': 13,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 3,
            'NewEventReward': 10,
            'LocationID': 24,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 4,
            'NewEventReward': 10,
            'LocationID': 5,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 5,
            'NewEventReward': 0,
            'LocationID': 34,
            'MapStatus': 0,
            'TextEntry': None,
            'Modifiers': []
        },




        {
            'EventIndex': 7,
            'NewEventReward': 2,
            'LocationID': 21,
            'MapStatus': 2,
            'TextEntry': "TID_WEEKEND_EVENT",
            'Modifiers': []
        }
    ]
    
    
    ComingUpEventsData = [
        {
            'EventIndex': 1,
            'NewEventReward': 10,
            'LocationID': 7,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 2,
            'NewEventReward': 10,
            'LocationID': 13,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 3,
            'NewEventReward': 10,
            'LocationID': 24,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 4,
            'NewEventReward': 10,
            'LocationID': 5,
            'MapStatus': 2,
            'TextEntry': None,
            'Modifiers': []
        },



        {
            'EventIndex': 5,
            'NewEventReward': 0,
            'LocationID': 34,
            'MapStatus': 0,
            'TextEntry': None,
            'Modifiers': []
        },




        {
            'EventIndex': 7,
            'NewEventReward': 2,
            'LocationID': 21,
            'MapStatus': 2,
            'TextEntry': "TID_WEEKEND_EVENT",
            'Modifiers': []
        }
    ]


class EventDataActiveEvent(Writer):
    def encode(self):
        EventsCount = len(EventSlots.EventsData)
        self.writeVInt(EventsCount) # Event Slots Count
        for map in EventSlots.EventsData:
            self.writeVInt(0)
            self.writeVInt(map['EventIndex']) # Event ID
            self.writeVInt(0) # New Event Timer 
            self.writeVInt(Utils.EventTimer(self)) # Event Timer
            self.writeVInt(map['NewEventReward']) # New Event Reward Amount
            self.writeDataReference(15, map['LocationID']) # Location ID
            self.writeVInt(map['MapStatus']) # Event Status 
            self.writeString(map['TextEntry']) # Event Text Entry
            self.writeVInt(0) # Boxes Purchased
            self.writeArrayVInt(map['Modifiers']) # Event Mofifiers
            self.writeVInt(0) # Ticketed Events Difficulty


class EventDataUpcomingEvent(Writer):
    def encode(self):
        EventsCount = len(EventSlots.ComingUpEventsData)
        self.writeVInt(EventsCount) # Event Slots Count
        for map in EventSlots.ComingUpEventsData:
            self.writeVInt(0)
            self.writeVInt(map['EventIndex']) # Event ID
            self.writeVInt(Utils.EventTimer(self)) # New Event Timer 
            self.writeVInt(Utils.EventTimer(self)) # Event Timer
            self.writeVInt(map['NewEventReward']) # New Event Reward Amount
            self.writeDataReference(15, map['LocationID']) # Location ID
            self.writeVInt(map['MapStatus']) # Event Status 
            self.writeString(map['TextEntry']) # Event Text Entry
            self.writeVInt(0) # Boxes Purchased
            self.writeArrayVInt(map['Modifiers']) # Event Mofifiers
            self.writeVInt(0) # Ticketed Events Difficulty