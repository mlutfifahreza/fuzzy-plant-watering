class Height:
    # T = {Small, Medium, Big}
    def __init__(self, min=0, max=100):
        self.min = min
        self.max = max
    
    # FUZZIFIER FUNCTIONS
    def getSmallValue(self, val):
        a = 0
        b = 17
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getMediumValue(self, val):
        c = 15
        d = 28
        e = 40
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        elif val < e :
            return (val-d)/(e-d)
        else :
            return 1
    def getBigValue(self, val):
        f = 50
        g = 100
        if val < f :
            return 0
        elif val < g :
            return (val-f)/(g-f)
        else :
            return 1