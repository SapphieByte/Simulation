import time, math, os, json, sys
import data as enum
from Person import Person
from Events import getEvent
from time import sleep as wait
from Plot import plot as _Plot
from inspect import signature

def set_resp(e, v):
    tempv = {}
    with open("resp.json", "r") as j:
        tempv = json.load(j)
    
    tempv[e] = v

    with open("resp.json", "w") as j:
        json.dump(tempv, j)

def get_events():
    with open("events.json", "r") as j:
        try:
            return json.load(j)
        except:
            return {}

def reset_events():
    with open("events.json", "w") as j:
        j.write("{}")

def reset_resp():
    with open("resp.json", "w") as j:
        j.write("{}")

def set_event(e, v):
    tempv = {}
    with open("events.json", "r") as j:
        tempv = json.load(j)
    
    tempv[e] = v

    with open("events.json", "w") as j:
        json.dump(tempv, j)

def do(genlimit, SAMPLE_SIZE, LIFESPAN, chance):
    os.system("start controller.pyw")
    gen = 0
    event = None
    gen_end_event = -1
    tt = 0
    graphdata = [[], [], [], [], []] # [employed, average money, 100s of people, 100s of people all-time, 100s of people died all-time]

    sample = []
    sample_employed = 0
    sample_dead = 0
    sample_average_money = 0
    sample_money_values = []
    sample_total_people = SAMPLE_SIZE
    cont = True

    for i in range(SAMPLE_SIZE):
        sample.append([Person(LIFESPAN), i+1])

    while len(sample) > 0 and gen <= genlimit and cont:
        gen += 1

        events = get_events()

        if "Close" in events:
            if events["Close"] == True:
                reset_events()

                set_resp("Close", True)
                
                cont = False

        if "Event" in events:
            if events["Event"] == True:
                set_event("Event", False)
                event = getEvent(101, bypass=True)
                gen_end_event = gen + event[0]

        if "Pause" in events:
            if events["Pause"] == True:
                set_event("Pause", False)
                _Plot(graphdata)
                set_resp("Pause", True)
        
        if cont:
            if event == None:
                event = getEvent(gen, chance=chance)
                if event != None:
                    gen_end_event = gen + event[0]
            else:
                if gen_end_event == gen:
                    set_resp("Event",  True)
                    event = None
            
            st = time.time()
            sample_money_values = []
            sample_average_money = 0
            
            for i in sample:
                if event != None:
                    i[0].event(event[1])
                i[0].update()
                res = i[0].check_for_reproduce()

                if res != None:
                    for y in range(res):
                        sample.append([Person(LIFESPAN, dependancy=i[0]), y+1])
                        sample_total_people += 1

                if i[0].Dead == True:
                    sample.remove(i)
                    sample_dead += 1
                    if i[0].Job != None:
                        sample_employed -= 1
                        if sample_employed < 0:
                            sample_employed = 0
                else:
                    sample_money_values.append(i[0].Money)

                if i[0].LastGenGotJob == True:
                    sample_employed += 1
                    i[0].LastGenGotJob = False
                elif i[0].LastGenLostJob == True:
                    sample_employed -= 1
                    if sample_employed < 0:
                        sample_employed = 0

                    i[0].LastGenLostJob == False


            for x in sample_money_values:
                sample_average_money += x

            sample_average_money /= len(sample_money_values)+1

            graphdata[0].append(sample_employed/100)
            graphdata[1].append(sample_average_money)
            graphdata[2].append(len(sample)/100)
            graphdata[3].append(sample_total_people/100)
            graphdata[4].append(sample_dead/100)
            

            ct = time.time()-st
            tt += ct

            if event == None:
                et = "None"
            else:
                et = f"{event[2]} ({gen_end_event-gen} loops remaining)"

            print(f"Gen {gen} took {ct}s (Spent {tt}s in total);\n    {sample_total_people} Spawned all-time, ({len(sample)} alive)\n    Current Event: {et}")

    _Plot(graphdata)

    if input("Save data? (y/n)\n    :: ").lower() == "y":
        name = str(math.floor(time.time())) + ".simsave"
        with open(f"./saves/{name}", "w+") as f:
            f.write("{\"value\":data}".replace("data", str(graphdata)))

        print(f"Successfully saved as {name}!")
    if input("Continue? (y/n)\n    :: ").lower() == "y":
        handle()
    else:
        set_resp("Close", True)
        reset_events()
        reset_resp()
        sys.exit()

def handle():
    reset_events()
    reset_resp()

    string = input("What would you like to do? (simulate/open)\n    :: ")

    if string.lower() in ["simulate", "sim"]:
        val = input("Genlimit, Sample Size, Lifespan, %Chance of Event = \n    :: ").replace(" ", "").split(",")
        
        if len(val) == len(signature(do).parameters):
            do(*[int(val[0]), int(val[1]), int(val[2]), float(val[3])*10000000])
        else:
            print(f"{len(val)} Parameters provided, expected {len(signature(do).parameters)}!")
            handle()
    elif string.lower() in ["open", "open file", "file"]:
        files = [f for f in os.listdir("./saves") if f.endswith("simsave")]
        if len(files) == 0:
            print("Sorry! No Sim Files were found.")

            if input("Continue? (y/n)\n    :: ").lower() == "y":
                handle()
        else:
            index = 0
            for e in files:
                index += 1
                print(f"      > {e} [{str(index)}]")

            file_ = input("\nWhich index would you like to open?\n    :: ")
            
            index = int(file_)-1

            filepath = f"./saves/{files[index]}"

            with open(filepath, "r") as f:
                _Plot(json.loads(f.read())["value"])

            if input("Continue? (y/n)\n    :: ").lower() == "y":
                handle()

    else:
        print("Invalid response.")
        handle()
handle()