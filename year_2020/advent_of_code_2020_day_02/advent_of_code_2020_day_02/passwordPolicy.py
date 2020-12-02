
class PasswordPolicy:
    def __init__(self, requiredCharacter, minCountOfInstances, maxCountOfinstances):
        self.requiredCharacter = requiredCharacter
        self.minNumberOfInstances = minCountOfInstances
        self.maxNumberOfInstances = maxCountOfinstances

    def isPasswordValid(self, passwordToTest):
        numberOfCharacterInstances = passwordToTest.count(self.requiredCharacter)

        if numberOfCharacterInstances >= self.minNumberOfInstances and  numberOfCharacterInstances <= self.maxNumberOfInstances:
            return True
        else:
            return False

def parsePasswordPolicyFromString(policyString):
    firstSplit = policyString.split('-', 1)
    minInstances = int(firstSplit[0].strip())

    secondSplit = firstSplit[1].split(' ', 1)
    maxInstances = int(secondSplit[0].strip())

    requiredCharacter = secondSplit[1].strip()

    return PasswordPolicy(requiredCharacter, minInstances, maxInstances)