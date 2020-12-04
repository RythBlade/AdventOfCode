
class Passport:

    def __init__(self, passportString):
        self.__passportString = passportString.strip() # sanitise the string
        self.parsedSuccess = True

        self.__dataDictionary = {}

        keyValuePairList = self.__passportString.split(" ")

        for pair in keyValuePairList:
            splitPair = pair.split(":")

            if(len(splitPair) != 2):
                self.__parsedSuccess = False
                return

            if splitPair[0] in self.__dataDictionary:
                print("Duplicate key!")
            else:
                self.__dataDictionary[splitPair[0]] = splitPair[1]

    def isPassportValid(self):
        toReturn = True

        toReturn = toReturn and ("byr" in self.__dataDictionary)
        toReturn = toReturn and ("iyr" in self.__dataDictionary)
        toReturn = toReturn and ("eyr" in self.__dataDictionary)
        toReturn = toReturn and ("hgt" in self.__dataDictionary)
        toReturn = toReturn and ("hcl" in self.__dataDictionary)
        toReturn = toReturn and ("ecl" in self.__dataDictionary)
        toReturn = toReturn and ("pid" in self.__dataDictionary)
        #toReturn = toReturn and ("cid" in self.__dataDictionary) # "cid" is optional for part 1

        return toReturn


def parsePassportsFromLines(passportLines):
    passports = []
    numberOfLines = len(passportLines)

    if numberOfLines > 0:
        nextPassport = ""
        lineIdx = 0

        while lineIdx < numberOfLines:
            trimmedLine = passportLines[lineIdx].strip()
        
            if len(trimmedLine) > 0: # is the line more than white space
                # yes - add it to the current passport string
                nextPassport += " " + trimmedLine # maintain the space separation between elements in the passport
            else:
                # it's a blank line - therefore the current passport is complete - add it to the list
                passports.append(Passport(nextPassport))
                nextPassport = ""
        
            lineIdx += 1

        if len(nextPassport) > 0 and nextPassport != "":
            passports.append(Passport(nextPassport)) # just in case we have left over data (maybe the last "new line" character at the end of the file was cropped by the file read for instance)

    return passports