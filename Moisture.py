class Moisture:
    # T = {Dry, Wet}
    def __init__(self, min=0, max=50):
        self.min = min
        self.max = max

    def getDryValue(self, val):
        if val < 5 :
            return 1
        elif val < 15 :
            return (15-val)/10
        else :
            return 0
    
    def getMoistValue(self, val):
        if val < 10 :
            return 0
        elif val < 20 :
            return (val-10)/10
        elif val < 30 :
            return (30-val)/10
        else :
            return 0
    
    def getWetValue(self, val):
        if val < 10 :
            return 0
        elif val < 30 :
            return (val-10)/20
        else :
            return 1

M = Moisture()
value = 18
print("dry\t:", M.getDryValue(value) )
print("moist\t:", M.getMoistValue(value) )
print("wet\t:", M.getWetValue(value) )