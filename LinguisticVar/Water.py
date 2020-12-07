import math

class Water:
    # T = {Little, Lots}
    def __init__(self, min=0, max=600):
        self.min = min
        self.max = max

    # FUZZIFIER FUNCTIONS
    def getLittleValue(self, val):
        a = 120
        b = 240
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getLotsValue(self, val):
        c = 200
        d = 600
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        else :
            return 1
        
    # DEFUZZIFIER FUNCTIONS
    # Rather Little
    def getRatherLittleDomain(self, val):
        a = 120
        b = 240
        return b - val*val*(b-a)
    
    # Little
    def getLittleDomain(self, val):
        a = 120
        b = 240
        return b - val*(b-a)
    
    # Very Little
    def getVeryLittleDomain(self, val):
        a = 120
        b = 240
        return b - math.sqrt(val)*(b-a)
    
    # Rather Lots
    def getRatherLotsDomain(self, val):
        c = 200
        d = 600
        return c + val*val*(d-c)

    # Lots
    def getLotsDomain(self, val):
        c = 200
        d = 600
        return c + val*(d-c)

    # Very Lots
    def getVeryLotsDomain(self, val):
        c = 200
        d = 600
        return c + math.sqrt(val)*(d-c)