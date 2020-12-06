from LinguisticVar.Moisture import Moisture
from LinguisticVar.Intensity import Intensity
from LinguisticVar.Leaves import Leaves
from LinguisticVar.Water import Water
from LinguisticVar.Height import Height
from LinguisticVar.Temperature import Temperature

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
        # # count and update value for intensity
        # term = self.intensity
        # if term == "dark":
        #     value = min(value, self.I.getDarkValue(i))
        # elif term == "bright":
        #     value = min(value, self.I.getBrightValue(i))
        # # count and update value for leaves
        # term = self.leaves
        # if term == "few":
        #     value = min(value, self.L.getFewValue(l))
        # elif term == "many":
        #     value = min(value, self.L.getManyValue(l))
        # count and update value for height
        term = self.height
        if term == "small":
            value = min(value, self.H.getSmallValue(h))
        elif term == "medium":
            value = min(value, self.H.getMediumValue(h))
        elif term == "big":
            value = min(value, self.H.getBigValue(h))
        term = self.temperature
        if term == "cold":
            value = min(value, self.T.getColdValue(t))
        elif term == "normal":
            value = min(value, self.T.getNormalValue(t))
        elif term == "hot":
            value = min(value, self.T.getHotValue(t))
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
            volume = self.W.geVerytLotsDomain(value)
        return value, volume


# Objects for Linguistic Variable
M,T,H,W = Moisture(), Temperature(), Height(), Water()
LinguisticVar = (M,T,H,W)

# ADDING RULES
terms = [
    ("dry","cold","small","little"),
    # ("dry","cold","small","lots"),
    ("dry","cold","medium","little"),
    ("dry","cold","medium","lots"),
    ("dry","cold","big","little"),
    ("dry","cold","big","lots"),
    ("dry","normal","small","little"),
    # ("dry","normal","small","lots"),
    ("dry","normal","medium","little"),
    ("dry","normal","medium","lots"),
    # ("dry","normal","big","little"),
    ("dry","normal","big","lots"),
    ("dry","hot","small","little"),
    ("dry","hot","small","lots"),
    # ("dry","hot","medium","little"),
    ("dry","hot","medium","lots"),
    # ("dry","hot","big","little"),
    ("dry","hot","big","lots"),
    ("moist","cold","small","little"),
    # ("moist","cold","small","lots"),
    ("moist","cold","medium","little"),
    # ("moist","cold","medium","lots"),
    ("moist","cold","big","little"),
    ("moist","cold","big","lots"),
    ("moist","normal","small","little"),
    # ("moist","normal","small","lots"),
    ("moist","normal","medium","little"),
    ("moist","normal","medium","lots"),
    ("moist","normal","big","little"),
    ("moist","normal","big","lots"),
    ("moist","hot","small","little"),
    ("moist","hot","small","lots"),
    ("moist","hot","medium","little"),
    ("moist","hot","medium","lots"),
    ("moist","hot","big","little"),
    ("moist","hot","big","lots"),
    ("wet","cold","small","little"),
    # ("wet","cold","small","lots"),
    ("wet","cold","medium","little"),
    # ("wet","cold","medium","lots"),
    ("wet","cold","big","little"),
    ("wet","cold","big","lots"),
    ("wet","normal","small","little"),
    # ("wet","normal","small","lots"),
    ("wet","normal","medium","little"),
    ("wet","normal","medium","lots"),
    ("wet","normal","big","little"),
    ("wet","normal","big","lots"),
    ("wet","hot","small","little"),
    # ("wet","hot","small","lots"),
    ("wet","hot","medium","little"),
    ("wet","hot","medium","lots"),
    ("wet","hot","big","little"),
    ("wet","hot","big","lots"),
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
moistureValue = int(input("moisture : "))
temperatureValue = int(input("temperature : "))
heightValue = int(input("height : "))

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