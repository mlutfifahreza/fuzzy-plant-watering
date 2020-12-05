from LinguisticVar.Moisture import Moisture
from LinguisticVar.Intensity import Intensity
from LinguisticVar.Leaves import Leaves
from LinguisticVar.Water import Water

def testVariablesFunction():
    M = Moisture()
    value = 18
    print("Moisture value =",value)
    print("dry\t:", M.getDryValue(value) )
    print("moist\t:", M.getMoistValue(value) )
    print("wet\t:", M.getWetValue(value) )
    print()

    I = Intensity()
    value = 40
    print("Intensity value =",value)
    print("dark\t:", I.getDarkValue(value))
    print("bright\t:", I.getBrightValue(value))
    print()

    L = Leaves()
    value= 90
    print("Leaves value =",value)
    print("Few\t:", L.getFewValue(value))
    print("Lots\t:", L.getManyValue(value))
    print()

    L = Water()
    value = 150
    print("Water value =",value)
    little = L.getLittleValue(value)
    lots = L.getLotsValue(value)
    print(value,"->",little,"->",L.getLittleDomain(little))
    print(value,"->",lots,"->",L.getLotsDomain(lots))
    print()
# testVariablesFunction()

class Rule:
    def __init__(self, lingustics=(), terms=()):
        self.M, self.I, self.L, self.W = lingustics
        self.moisture, self.intensity, self.leaves, self.water = terms
    
    def getInferenceValue(self, vars=()):
        m,i,l = vars
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
        # count and update value for leaves
        term = self.leaves
        if term == "few":
            value = min(value, self.L.getFewValue(l))
        elif term == "many":
            value = min(value, self.L.getManyValue(l))
        # find the value of watering
        volume = 0
        term = self.water
        if term == "little":
            volume = self.W.getLittleDomain(value)
        elif term == "lots":
            volume = self.W.getLotsDomain(value)
        return value, volume

# Linguistic Variable Objects
M,I,L,W = Moisture(), Intensity(), Leaves(), Water()
LinguisticVar = (M,I,L,W)
# Linguistic Term for each rules
terms1 = ("dry","bright","many","lots")
rule1 = Rule(LinguisticVar, terms1)

# Testing
moistureValue = 6
intensityValue = 50
leavesValue = 80
vars = (moistureValue, intensityValue, leavesValue)
testValue, testVolume = rule1.getInferenceValue(vars)
print("Watering value = ", testValue)
print("Watering volume = ", testVolume, "ml")