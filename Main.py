import time, math
import data as enum
from Person import Person
from Events import getEvent
from time import sleep as wait
from Plot import plot as _Plot

def do(genlimit, SAMPLE_SIZE, LIFESPAN):
    gen = 0
    event = None
    gen_end_event = -1
    tt = 0
    graphdata = [[], [], [], [], []] # [employed, average money, 100s of people, 100s of people all-time, 100s of people died all-time]

    sample = []
    sample_is_dead = False
    sample_employed = 0
    sample_unemployed = SAMPLE_SIZE
    sample_dead = 0
    sample_average_money = 0
    sample_money_values = []
    sample_total_people = SAMPLE_SIZE
    sample_jobs = [[0], [0], [0], [0], [0], [0]]

    for i in range(SAMPLE_SIZE):
        sample.append([Person(LIFESPAN), i+1])

    while len(sample) > 0 and gen <= genlimit:
        gen += 1

        if event == None:
            event = getEvent(gen)
            if event != None:
                gen_end_event = gen + event[0]
        else:
            if gen_end_event == gen:
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
                temp = sample_jobs[int(i[0].Job)-1]
                sample_jobs[int(i[0].Job)-1].append(temp[len(temp)-1]+1)
                i[0].LastGenGotJob = False
            elif i[0].LastGenLostJob == True:
                sample_employed -= 1
                if sample_employed < 0:
                    sample_employed = 0

                temp = sample_jobs[int(i[0].CachedJob)-1]
                sample_jobs[int(i[0].CachedJob)-1].append(temp[len(temp)-1]-1)
                i[0].LastGenLostJob == False


        for x in sample_money_values:
            sample_average_money += x

        sample_average_money /= len(sample_money_values)+1

        graphdata[0].append(sample_employed)
        graphdata[1].append(sample_average_money)
        graphdata[2].append(len(sample)/100)
        graphdata[3].append(sample_total_people/100)
        graphdata[4].append(sample_dead/100)
        

        ct = time.time()-st
        tt += ct

        if event == None:
            et = "None"
        else:
            et = event[2]

        print(f"Gen {gen} took {ct}s (Spent {tt}s in total);\n    {sample_total_people} Spawned all-time, ({len(sample)} alive)\n    Current Event: {et}")

    print(sample_jobs)

    for t in sample_jobs:
        graphdata.append(t)

    _Plot(graphdata)

val = input("Genlimit, Sample Size, Lifespan = \n    :: ").replace(" ", "").split(",")

do(*[int(val[0]), int(val[1]), int(val[2])])