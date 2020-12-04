class Intensity:
    # T = {Dry, Wet}
    def __init__(self, min=0, max=100):
        self.min = min
        self.max = max

    def getDarkValue(self, val):
        if val < 10 :
            return 1
        elif val < 25 :
            return ((25-val)/15)
        else :
            return 0
    
    def getDimValue(self, val):
        if val < 20 :
            return 0
        elif val < 35 :
            return (val-20)/15
        elif val < 50 :
            return (50-val)/15
        else :
            return 0

    def getBrightValue(self, val):
        if val < 40 :
            return 0
        elif val < 70 :
            return ((val-40)/30)
        else :
            return 1