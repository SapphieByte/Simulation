import math
import random
import data as enum

events = enum.events

def getEvent(gen, chance=30000000, bypass=False):
    if gen > 100 and random.randint(1, 1000000000) < int(chance) or bypass == True:
        event = events[str(random.randint(1, len(events)))]

        return [ random.randint(event["duration"][0], event["duration"][1]), event["killchance"], event["name"] ]
    else:
        return None