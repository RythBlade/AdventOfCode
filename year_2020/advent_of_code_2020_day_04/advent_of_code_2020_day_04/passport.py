
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

    def isPassportValidPart1(self):
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

    def isPassportValidPart2(self):
        toReturn = self.isPassportValidPart1()

        if toReturn:
            byr = int(self.__dataDictionary["byr"])
            toReturn = toReturn and byr >= 1920 and byr <= 2002

            iyr = int(self.__dataDictionary["iyr"])
            toReturn = toReturn and iyr >= 2010 and iyr <= 2020

            eyr = int(self.__dataDictionary["eyr"])
            toReturn = toReturn and eyr >= 2020 and eyr <= 2030

            if toReturn:
                hgt = self.__dataDictionary["hgt"]
                hgtLength = len(hgt)
                if hgtLength > 2:
                    height = int(hgt[:hgtLength - 2])
                    unit = hgt[hgtLength - 2:hgtLength]

                    if unit == "cm":
                        toReturn = toReturn and height >= 150 and height <= 193
                    elif unit == "in":
                        toReturn = toReturn and height >= 59 and height <= 76
                    else:
                        toReturn = False
                else:
                    # There must be a 2 character unit + a number in the string
                    toReturn = False

            if toReturn:
                hcl = self.__dataDictionary["hcl"]
                hclLength = len(hcl)

                toReturn = toReturn and hclLength == 7
                toReturn = toReturn and hcl[0] == '#'

                if toReturn:
                    for character in range(1, 7):
                        if (hcl[character] >= '0' and hcl[character] <= '9') or (hcl[character] >= 'a' and hcl[character] <= 'f'):
                            pass
                        else:
                            toReturn = False
                            break

            if toReturn:
                ecl = self.__dataDictionary["ecl"]
                if ecl == "amb" or ecl == "blu" or ecl == "brn" or ecl == "gry" or ecl == "grn" or ecl == "hzl" or ecl == "oth":
                    pass
                else:
                    toReturn = False

            pid = self.__dataDictionary["pid"]
            toReturn = toReturn and pid.isdigit() and len(pid) == 9

            # don't need to validate cid

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