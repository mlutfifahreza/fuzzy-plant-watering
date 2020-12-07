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
        # print("Moisture is {0} AND Temperature is {1} AND Height is {2}".format(self.moisture, self.temperature, self.height))
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
print("\n---------------------------")
print("PLANT WATERING FUZZY SYSTEM")
print("---------------------------")
moistureValue = int(input("Moisture ({0}..{1})\t: ".format(M.min, M.max)))
temperatureValue = int(input("Temperature ({0}..{1})\t: ".format(T.min, T.max)))
heightValue = int(input("Height ({0}..{1}) \t: ".format(H.min, H.max)))

# PROCESSING
vars = (moistureValue, temperatureValue, heightValue)
totalVolume = 0
totalValue = 0
for i in range(len(rules)):
    testValue, testVolume = rules[i].getInferenceValue(vars)
    totalValue += testValue
    totalVolume += testValue*testVolume
    # print(i)
    # if (testValue > 0):
#         print("Value = {0}, Volume = {1}".format(testValue,testVolume))
#         print()
# print("Total volume =",totalVolume)
# print("Total value =",totalValue)
volume = 0
# preventing division by 0
try:
    volume = totalVolume/totalValue
except:
    volume = totalValue

# OUTPUT
print("\n<- Output ->")
print("Watering volume = ", int(volume), "ml")
input("\n> Press enter to exit")
print("-------- Made By --------")
print("> Dewa Nyoman Dharma")
print("> Fadhlan Pasyah")
print("> Muhammad Lutfi Fahreza")