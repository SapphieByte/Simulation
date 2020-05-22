import math
import random
import data as enum

events = enum.events

def getEvent(gen):
    if gen > 100 and random.randint(1, 1000) < 30:
        event = events[str(random.randint(1, len(events)))]

        return [ random.randint(event["duration"][0], event["duration"][1]), event["killchance"], event["name"] ]
    else:
        return None