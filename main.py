import json

elements = {}
with open('PeriodicTableJSON.json', 'r') as file:
    elements = json.load(file)["elements"]

print("Type in the element")
userInput = input("  -> ")

def GetAtomicMass(e): # returns the atomic mass of a given element
    for element in elements:
        if (element["symbol"] == e):
            return round(element["atomic_mass"], 1)
        
def GetElementName(e): # returns the atomic mass of a given element
    for element in elements:
        if (element["symbol"] == e):
            return element["name"]

def CalcMoleMass(molecule):
    eStr = "" # short for "element string"
    atomicMasses = [] # the atomic masses are stored here to be later used
    n = -1 # used to know what object to multiply in the "atomicMasses" list
    i = -1 # used to know what letter of the molecule str we are on
    skip = False
    for letter in molecule: # this for loop fills in the "atomicMasses" list
        i += 1
        if (skip):
            skip = False
            continue

        if (letter.isdigit()):
            try:
                if (molecule[i+1].isdigit()):
                    letter = int(letter + molecule[i+1])
                    skip = True
                else:
                    letter = int(letter)
            except:
                letter = int(letter)

            atomicMasses[n] *= letter
            print("x" + str(letter))
            continue

        try:
            if (molecule[i+1].lower() == molecule[i+1] and molecule[i+1].isdigit() == False):
                skip = True

                eStr = letter + molecule[i+1]
            else:
                eStr = letter
        except:
            eStr = letter

        atomicMass = GetAtomicMass(eStr)
        if (atomicMass != None):
            atomicMasses.append(atomicMass)
            print(GetElementName(eStr))
            n += 1

    # below the atomicMasses are added to get the result.
    moleMass = 0
    for n in atomicMasses: 
        moleMass += n
    return moleMass

print("Mole Mass:", CalcMoleMass(userInput))