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

validPassports = 0
passportsThatFailedToParse = 0

for nextPassport in passports:
    if nextPassport.parsedSuccess:
        if nextPassport.isPassportValid():
            validPassports += 1
        else:
            print("invalid, {0}".format(nextPassport._Passport__passportString))
    else:
        passportsThatFailedToParse += 1

print("Passports failed to parse, {0}".format(passportsThatFailedToParse))
print("Valid Passports, {0}".format(validPassports))
print("Application complete. Time taken(s), {0}".format(applicationTimer.elapsedTime()))