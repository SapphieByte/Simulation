import random
import data as enum
import math

class Person:
    def __init__(self, ls, dependancy=None):
        self.Trait = str(random.randint(1, len(enum.traits)))
        self.Job = None
        self.Age = 0
        self.Lifespan = ls
        self.Dead = False
        self.LastGenGotJob = False
        self.FoodRequirement = random.randint(8, 12)
        self.Food = self.FoodRequirement
        self.Actions = 3
        self.Money = 0
        self.CanGetJob = True
        self.LastGenLostJob = False
        self.CachedJob = None

        if random.randint(1, 100) < 40:
            self.CanBirth = False
        else:
            self.CanBirth = True

        if type(dependancy) == Person:
            self.Trait = dependancy.Trait
            self.FoodRequirement = dependancy.FoodRequirement
            self.CanBirth = dependancy.CanBirth

    def get_job(self):
        r = str(random.randint(1, len(enum.jobs)))
        found = enum.jobs[r]
        if self.Trait == found["preference"][0]:
            if random.randint(1, found["preference"][1]) < found["preference"][1] and self.CanGetJob == True:
                self.Job = r
                self.CachedJob = self.Job
                self.LastGenGotJob = True
        elif self.Trait != found["preference"][0]:
            if random.randint(1, found["preference"][2]) < found["preference"][2] and self.CanGetJob == True:
                self.Job = r
                self.CachedJob = self.Job
                self.LastGenGotJob = True
    
    def work(self):
        if self.Job != None:
            self.Money += enum.jobs[self.Job]["pay"]
    
    def update(self):
        self.Actions = 3

        if self.Age >= math.floor(self.Lifespan/5):
            self.Food -= 2
        
        if self.Dead == False:
            self.Age += 1

        target = self.Lifespan + random.randint(-5, 5)
        if self.Age >= target:
            self.Dead = True
            if self.Job != None:
                self.CachedJob = self.Job
                self.LastGenLostJob = True

        else:
            if self.Age >= math.floor(self.Lifespan/4.75) and self.Job == None:
                self.get_job()
            
            def rec():
                if self.Actions > 0:
                    if self.Food < self.FoodRequirement:
                        if self.Money >= 4:
                            self.Money -= 4
                            self.Food += 2
                            self.Actions -= 1
                            if self.Food < self.FoodRequirement:
                                rec()
            
            rec()

            if self.Food < self.FoodRequirement - 8:
                self.Dead = True
                if self.Job != None:
                    self.LastGenLostJob = True

            
            if self.Actions > 0 and self.Job != None:
                self.work()

            if self.Job != None and self.CanGetJob == True:
                if self.Age >= math.floor(self.Lifespan/2.5):
                    temp = self.Age-math.floor(self.Lifespan/2.5)
                    if 100-(temp*2) > 1:
                        if random.randint(1, 100-(temp*2)) == 1:
                            self.Job = None
                            self.CanGetJob = False
                            if self.Job != None:
                                self.LastGenLostJob = True

    
    def check_for_reproduce(self):
        if self.Age >= math.floor(self.Lifespan*0.45) and self.Actions > 0 and random.randint(1, 100) < 8 and self.CanBirth == True:
            if random.randint(1, 100) < 40:
                self.Dead = True
                if self.Job != None:
                    self.LastGenLostJob = True

            if random.randint(1, 100) < 25:
                self.CanBirth = False
            else:
                self.CanBirth = True

            return random.randint(1, 2)

    def event(self, e):
        if random.randint(1, 100) <= random.choice(e):
            self.Dead = True
            if self.Job != None:
                self.LastGenLostJob = True
