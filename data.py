traits = {
    "1": "None",
    "2": "Strong",
    "3": "Inteligent",
    "4": "Logic",
    "5": "Memory"
}

jobs = {
    "1": {
        "name": "Builder",
        "preference": ["2", 80, 8], # [trait id, chance if you have trait, chance if you don't have trait]
        "pay": 5
    },
    "2": {
        "name": "Scientist",
        "preference": ["3", 45, 2],
        "pay": 8
    },
    "3": {
        "name": "Accountant",
        "preference": ["4", 50, 15],
        "pay": 6
    },
    "4": {
        "name": "thief",
        "preference": ["-1", 8, 8], # No preference
        "pay": 13
    },
    "5": {
        "name": "Electrician",
        "preference": ["5", 60, 25],
        "pay": 5
    },
    "6": {
        "name": "Cashier/Fast Food worker",
        "preference": ["1", 90, 80],
        "pay": 2
    }
}

events = {
    "1": {
        "name": "Pandemic",
        "killchance": [3, 7],
        "duration": [12, 14]
    },
    "2": {
        "name": "Meteor",
        "killchance": [15, 35],
        "duration": [1, 1]
    },
    "3": {
        "name": "Famine",
        "killchance": [1, 4],
        "duration": [20, 65]
    },
    "4": {
        "name": "Nuclear Accident",
        "killchance": [20, 50],
        "duration": [1, 1]
    }
}