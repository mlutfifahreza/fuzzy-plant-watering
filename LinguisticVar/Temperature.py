class Temperature:
    # T = {Dry, Wet}
    def __init__(self, min=0, max=50):
        self.min = min
        self.max = max

    # FUZZIFIER FUNCTIONS
    def getColdValue(self, val):
        a = 15
        b = 25
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getNormalValue(self, val):
        b = 20
        c = 27
        d = 32
        if val < b :
            return 0
        elif val < c :
            return (val-b)/(c-b)
        elif val < d :
            return (d-val)/(d-c)
        else :
            return 0
    def getHotValue(self, val):
        c = 30
        d = 36
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        else :
            return 1