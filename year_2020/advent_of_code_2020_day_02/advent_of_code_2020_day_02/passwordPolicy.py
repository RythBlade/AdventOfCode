
class PasswordPolicy:
    def __init__(self, requiredCharacter, minCountOfInstances, maxCountOfinstances):
        self.requiredCharacter = requiredCharacter
        self.minNumberOfInstances = minCountOfInstances
        self.maxNumberOfInstances = maxCountOfinstances

    def isPasswordValidPart1(self, passwordToTest):
        numberOfCharacterInstances = passwordToTest.count(self.requiredCharacter)

        if numberOfCharacterInstances >= self.minNumberOfInstances and  numberOfCharacterInstances <= self.maxNumberOfInstances:
            return True
        else:
            return False

    def isPasswordValidPart2(self, passwordToTest):
        passwordLength = len(passwordToTest)

        zeroIndexFirst = self.minNumberOfInstances - 1
        zeroIndexSecond = self.maxNumberOfInstances - 1
        
        firstInstanceExists = False
        secondInstanceExists = False

        if zeroIndexFirst >= 0 and zeroIndexFirst < passwordLength:
            if passwordToTest[zeroIndexFirst] == self.requiredCharacter:
                firstInstanceExists = True

        if zeroIndexSecond >= 0 and zeroIndexSecond < passwordLength:
            if passwordToTest[zeroIndexSecond] == self.requiredCharacter:
                secondInstanceExists = True

        if (firstInstanceExists or secondInstanceExists) and (firstInstanceExists != secondInstanceExists):
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