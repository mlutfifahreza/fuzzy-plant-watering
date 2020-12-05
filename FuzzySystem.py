from LinguisticVar.Moisture import Moisture
from LinguisticVar.Intensity import Intensity
from LinguisticVar.Leaves import Leaves
from LinguisticVar.Water import Water
from LinguisticVar.Height import Height

class Rule:
    def __init__(self, lingustics=(), terms=()):
        self.M, self.I, self.H, self.W = lingustics
        self.moisture, self.intensity, self.height, self.water = terms
    
    def getInferenceValue(self, vars=()):
        m,i,h = vars
        value = 1
        # count and update value for moisture
        term = self.moisture
        if term == "dry":
            value = min(value, self.M.getDryValue(m))
        elif term == "moist":
            value = min(value, self.M.getMoistValue(m))
        elif term == "wet":
            value = min(value, self.M.getWetValue(m))
        # count and update value for intensity
        term = self.intensity
        if term == "dark":
            value = min(value, self.I.getDarkValue(i))
        elif term == "bright":
            value = min(value, self.I.getBrightValue(i))
        # # count and update value for leaves
        # term = self.leaves
        # if term == "few":
        #     value = min(value, self.L.getFewValue(l))
        # elif term == "many":
        #     value = min(value, self.L.getManyValue(l))
        # count and update value for height
        term = self.height
        if term == "small":
            value = min(value, self.H.getHeightValue(h))
        elif term == "medium":
            value = min(value, self.H.getHeightValue(h))
        elif term == "big":
            value = min(value, self.H.getHeightValue(h))
        # find the value of watering
        volume = 0
        term = self.water
        if term == "little":
            volume = self.W.getLittleDomain(value)
        elif term == "lots":
            volume = self.W.getLotsDomain(value)
        return value, volume


# Objects for Linguistic Variable
M,I,H,W = Moisture(), Intensity(), Height(), Water()
LinguisticVar = (M,I,H,W)

# ADDING RULES
terms = [
    ("dry","bright","many","lots"),
    ("dry","bright","many","little"),
    ]
rules = []
for term in terms:
    rules.append(Rule(LinguisticVar, term))

# INPUT VALUE
# Example
moistureValue = 6
intensityValue = 50
heightValue = 40
# Input from user (sensor)
moistureValue = int(input("moisture : "))
intensityValue = int(input("intensity : "))
heightValue = int(input("height : "))

# PROCESSING
vars = (moistureValue, intensityValue, heightValue)
output = 0
testValueSum = 0
for rule in rules:
    testValue, testVolume = rule.getInferenceValue(vars)
    testValueSum += testValue
    output += testValue*testVolume
output /= testValueSum

# OUTPUT
print("Watering volume = ", int(output), "ml")