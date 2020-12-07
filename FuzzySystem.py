from LinguisticVar.Moisture import Moisture
from LinguisticVar.Temperature import Temperature
from LinguisticVar.Height import Height
from LinguisticVar.Water import Water

class Rule:
    def __init__(self, lingustics=(), terms=()):
        self.M, self.T, self.H, self.W = lingustics
        self.moisture, self.temperature, self.height, self.water = terms
    
    def getInferenceValue(self, vars=()):
        m,t,h = vars
        value = 1
        # count and update value for moisture
        term = self.moisture
        if term == "dry":
            value = min(value, self.M.getDryValue(m))
        elif term == "moist":
            value = min(value, self.M.getMoistValue(m))
        elif term == "wet":
            value = min(value, self.M.getWetValue(m))
        # count and update value for temperature
        term = self.temperature
        if term == "cold":
            value = min(value, self.T.getColdValue(t))
        elif term == "normal":
            value = min(value, self.T.getNormalValue(t))
        elif term == "hot":
            value = min(value, self.T.getHotValue(t))
        # count and update value for height
        term = self.height
        if term == "small":
            value = min(value, self.H.getSmallValue(h))
        elif term == "medium":
            value = min(value, self.H.getMediumValue(h))
        elif term == "big":
            value = min(value, self.H.getBigValue(h))
        # find the value of watering
        volume = 0
        term = self.water
        if term == "little":
            volume = self.W.getLittleDomain(value)
        elif term == "rather little":
            volume = self.W.getRatherLittleDomain(value)
        elif term == "very little":
            volume = self.W.getVeryLittleDomain(value)
        elif term == "lots":
            volume = self.W.getLotsDomain(value)
        elif term == "rather lots":
            volume = self.W.getRatherLotsDomain(value)
        elif term == "very lots":
            volume = self.W.getVeryLotsDomain(value)
        # function output
        return value, volume


# Objects for Linguistic Variable
M,T,H,W = Moisture(), Temperature(), Height(), Water()
LinguisticVar = (M,T,H,W)

# ADDING RULES
terms = [
    # LITTLE PLANT
    # very little
    ("wet","cold","small","very little"),
    ("wet","normal","small","very little"),
    # little
    ("wet","hot","small","little"),
    ("moist","cold","small","little"),
    ("moist","normal","small","little"),
    # rather little
    ("moist","hot","small","rather little"),
    ("dry","cold","small","rather little"),
    # rather lots
    ("dry","normal","small","rather lots"),
    ("dry","hot","small","rather lots"),
    # lots
    # very lots
    
    # MEDIUM PLANT
    # very little
    # little
    ("wet","cold","medium","little"),
    ("wet","normal","medium","little"),
    # rather little
    ("wet","hot","medium","rather little"),
    ("moist","cold","medium","rather little"),
    # rather lots
    ("moist","normal","medium","rather lots"),
    ("moist","hot","medium","rather lots"),
    # lots
    ("dry","cold","medium","lots"),
    ("dry","normal","medium","lots"),
    # very lots
    ("dry","hot","medium","very lots"),
    
    # BIG PLANT
    # very little
    # little
    # rather little
    # rather lots
    ("wet","cold","big","rather lots"),
    ("wet","normal","big","rather lots"),
    # lots
    ("wet","hot","big","lots"),
    ("moist","cold","big","lots"),
    ("moist","normal","big","lots"),
    ("moist","hot","big","lots"),
    ("dry","cold","big","lots"),
    # very lots
    ("dry","normal","big","very lots"),
    ("dry","hot","big","very lots"),
]
rules = []
for term in terms:
    rules.append(Rule(LinguisticVar, term))

# INPUT VALUE
# Example
moistureValue = 6
temperatureValue = 50
heightValue = 40
# Input from user (sensor)
# moistureValue = int(input("moisture : "))
# temperatureValue = int(input("temperature : "))
# heightValue = int(input("height : "))

# PROCESSING
vars = (moistureValue, temperatureValue, heightValue)
output = 0
testValueSum = 0
for rule in rules:
    testValue, testVolume = rule.getInferenceValue(vars)
    testValueSum += testValue
    output += testValue*testVolume
output /= testValueSum

# OUTPUT
print("Watering volume = ", int(output), "ml")