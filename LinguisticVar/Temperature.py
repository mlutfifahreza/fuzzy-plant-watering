class Temperature:
    # T = {Dry, Wet}
    def __init__(self, min=0, max=50):
        self.min = min
        self.max = max

    # FUZZIFIER FUNCTIONS
    def getColdValue(self, val):
        a = 18
        b = 22
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getNormalValue(self, val):
        b = 18
        c = 24
        d = 30
        if val < b :
            return 0
        elif val < c :
            return (val-b)/(c-b)
        elif val < d :
            return (d-val)/(d-c)
        else :
            return 0
    def getHotValue(self, val):
        c = 27
        d = 30
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        else :
            return 1