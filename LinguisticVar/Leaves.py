class Leaves:
    # T = {Few, Many}
    def __init__(self, min=0, max=200):
        self.min = min
        self.max = max
    
    # FUZZIFIER FUNCTIONS
    def getFewValue(self, val):
        a = 30
        b = 60
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getManyValue(self, val):
        c = 50
        d = 100
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        else :
            return 1