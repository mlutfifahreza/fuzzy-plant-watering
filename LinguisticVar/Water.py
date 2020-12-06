import math

class Water:
    # T = {Little, Lots}
    def __init__(self, min=0, max=600):
        self.min = min
        self.max = max

    # FUZZIFIER FUNCTIONS
    def getLittleValue(self, val):
        a = 75
        b = 200
        if val < a :
            return 1
        elif val < b :
            return (b-val)/(b-a)
        else :
            return 0
    def getLotsValue(self, val):
        c = 150
        d = 400
        if val < c :
            return 0
        elif val < d :
            return (val-c)/(d-c)
        else :
            return 1
        
    # DEFUZZIFIER FUNCTIONS
    # Rather Little
    def getRatherLittleDomain(self, val):
        a = 75
        b = 200
        return b - val*val*(b-a)
    
    # Little
    def getLittleDomain(self, val):
        a = 75
        b = 200
        return b - val*(b-a)
    
    # Very Little
    def getVeryLittleDomain(self, val):
        a = 75
        b = 200
        return b - math.sqrt(val)*(b-a)
    
    # Rather Lots
    def getRatherLotsDomain(self, val):
        c = 150
        d = 400
        return c + val*val*(d-c)

    # Lots
    def getLotsDomain(self, val):
        c = 150
        d = 400
        return c + val*(d-c)

    # Very Lots
    def getVeryLotsDomain(self, val):
        c = 150
        d = 400
        return c + math.sqrt(val)*(d-c)