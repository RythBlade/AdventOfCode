from Timer import Timer
import passport

def loadPassportBatch(filename):
    with open(filename) as file:
        return file.readlines()

applicationTimer = Timer()

print("Application Started")

passportFilename = "passport_batch.txt"
passportFile = loadPassportBatch(passportFilename)

passports = passport.parsePassportsFromLines(passportFile)

print("Passports found, {0}".format(len(passports)))

validPassportsPart1 = 0
validPassportsPart2 = 0
passportsThatFailedToParse = 0

passportId = 0

for passportId in range(len(passports)):
    if passports[passportId].parsedSuccess:
        if passports[passportId].isPassportValidPart1():
            validPassportsPart1 += 1

        if passports[passportId].isPassportValidPart2():
            validPassportsPart2 += 1
    else:
        passportsThatFailedToParse += 1

print("Passports failed to parse, {0}".format(passportsThatFailedToParse))
print("Valid Passports part 1, {0}".format(validPassportsPart1))
print("Valid Passports part 2, {0}".format(validPassportsPart2))
print("Application complete. Time taken(s), {0}".format(applicationTimer.elapsedTime()))