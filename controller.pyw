import pygame
pygame.init()

import sys, time, json

screen = pygame.display.set_mode((500, 500))

font = pygame.font.Font("InconsolataExpanded-Regular.ttf", 14)

et = font.render("Press [E] to spawn an event", True, (230, 230, 235))
st = font.render("Press [S] to stop the simulation.", True, (230, 230, 235))
pt = font.render("Press [P] to pause the simulation.", True, (230, 230, 235))

current_events = []

def set_event(e, v):
    tempv = {}
    with open("events.json", "r") as j:
        tempv = json.load(j)
    
    tempv[e] = v

    with open("events.json", "w") as j:
        json.dump(tempv, j)

def get_resp():
    with open("resp.json", "r") as j:
        try:
            return json.load(j)
        except:
            return {}

def reset_resp():
    with open("resp.json", "w") as j:
        j.write("{}")

def set_resp(e, v):
    tempv = {}
    with open("resp.json", "r") as j:
        tempv = json.load(j)
    
    tempv[e] = v

    with open("resp.json", "w") as j:
        json.dump(tempv, j)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            set_event("Close", True)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == 101:
                if "event" not in current_events:
                    current_events.append("event")
                    set_event("Event", True)
            elif event.key == 115:
                set_event("Close", True)
                sys.exit()
            elif event.key == 112:
                if "pause" not in current_events:
                    current_events.append("pause")
                    set_event("Pause", True)
            print(event)
        
    screen.fill((0, 0, 0))
    
    screen.blit(et, (0, 0))
    screen.blit(st, (0, 20))
    screen.blit(pt, (0, 40))

    resp = get_resp()

    if "Event" in resp:
        if resp["Event"] == True:
            if "event" in current_events:
                current_events.remove("event")
                set_event("Event", False)
                set_resp("Event", False)

    if "Close" in resp:
        if resp["Close"] == True:
            set_event("Close", False)
            reset_resp()
            sys.exit()

    if "Pause" in resp:
        if resp["Pause"] == True:
            set_event("Pause", False)
            current_events.remove("pause")
            set_resp("Pause", False)

    pygame.display.flip()

    time.sleep(1/60)