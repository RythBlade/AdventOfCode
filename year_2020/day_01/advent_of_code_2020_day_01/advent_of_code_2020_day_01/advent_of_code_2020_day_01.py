
from Timer import Timer

fileExpenses = []
expenseFileName = "expenses_input.txt"

def readExpensesFile(filename):
    readExpenses = []
    # read in the file contents - each value is an int on an individual line
    with open(filename) as file:
        lines = file.readlines()

        for line in lines:
            readExpenses.append(int(line))

    return readExpenses

def partOneFind2NumbersThatSum(total, expenseList):
    multipliedAnswer = 0
    countOfElements = len(expenseList)
    foundPair = False

    #compare each element to each element AFTER it in the list, to avoid duplicate comparisons
    for firstIdx in range(countOfElements):
        for secondIdx in range(firstIdx + 1, countOfElements): # start the inner loop from next element so we don't compare against ourselves
            firstNum = expenseList[firstIdx]
            secondNum = expenseList[secondIdx]

            if firstNum + secondNum == total:
                multipliedAnswer = firstNum * secondNum
                print("Found two numbers summing to " + str(total) + ". First, " + str(firstNum) + ", Second, " + str(secondNum) + ", Multiplied, " + str(multipliedAnswer))
                foundPair = True
                break

        if foundPair:
            break

    if foundPair:
        print("Successfully found a pair!")
    else:
        print("Failed to find pair")

def partTwoFind3NumbersThatSum(total, expenseList):
    multipliedAnswer = 0
    countOfElements = len(expenseList)
    foundTriplet = False

    #brute force - check every combination
    #if the list had been sorted - could start from the highest number, and then early out on combinations we know will be too large
    for firstIdx in range(countOfElements):
        for secondIdx in range(countOfElements):
            
            if firstIdx == secondIdx: # don't compare against ourselves
                continue

            firstNum = expenseList[firstIdx]
            secondNum = expenseList[secondIdx]

            firstPlusSecond = firstNum + secondNum

            if firstPlusSecond >= total: # have we already exceeded our target - in which case, nothing in the 3rd inner loop can succeed
                continue

            for thirdIdx in range(countOfElements):
                if secondIdx == thirdIdx and firstIdx == thirdIdx: # don't compare against ourselves
                    continue

                thirdNum = expenseList[thirdIdx]

                if thirdNum + firstPlusSecond == total:
                    multipliedAnswer = firstNum * secondNum * thirdNum
                    print("Found three numbers summing to " + str(total) + ". First, " + str(firstNum) + ", Second, " + str(secondNum) + ", Third, " + str(thirdNum) + ", Multiplied, " + str(multipliedAnswer))
                    foundTriplet = True
                    break

            if foundTriplet:
                break

        if foundTriplet:
            break
    
    if foundTriplet:
        print("Successfully found a triplet!")
    else:
        print("Failed to find triplet")

# MAIN
applicationTimer = Timer()
########################################################
fileLoadTimer = Timer()

fileExpenses = readExpensesFile(expenseFileName)

fileLoadTime = fileLoadTimer.elapsedTime()
print("File load complete. It took (s), " + str(fileLoadTime))
print("\n")

########################################################

partOneTimer = Timer()

partOneFind2NumbersThatSum(2020, fileExpenses)

partOneTime = partOneTimer.elapsedTime()
print("Part One. It took (s), " + str(partOneTime))
print("\n")

########################################################

partTwoTimer = Timer()

partTwoFind3NumbersThatSum(2020, fileExpenses)

partTwoTime = partTwoTimer.elapsedTime()
print("Part Two. It took (s), " + str(partTwoTime))
print("\n")

########################################################

applicationTime = applicationTimer.elapsedTime()
print("Application complete. It took (s), " + str(applicationTime))