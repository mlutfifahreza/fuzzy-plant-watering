class Moisture:
    # T = {Dry, Wet}
    def __init__(self, min=0, max=50):
        self.min = min
        self.max = max

    # FUZZIFIER FUNCTIONS
    def getDryValue(self, val):
        a = 5
        b = 15
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getMoistValue(self, val):
        b = 10
        c = 20
        d = 30
        if val < b :
            return 0
        elif val < c :
            return (val-b)/(c-b)
        elif val < d :
            return (d-val)/(d-c)
        else :
            return 0
    def getWetValue(self, val):
        c = 10
        d = 30
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        else :
            return 1