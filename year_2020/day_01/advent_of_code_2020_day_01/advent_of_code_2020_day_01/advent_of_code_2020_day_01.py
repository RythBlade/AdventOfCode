
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
    found2020Pair = False

    #compare each element to each element AFTER it in the list, to avoid duplicate comparisons
    for firstIdx in range(countOfElements):
        for secondIdx in range(firstIdx + 1, countOfElements): # start the inner loop from next element so we don't compare against ourselves
            firstNum = expenseList[firstIdx]
            secondNum = expenseList[secondIdx]

            if firstNum + secondNum == 2020:
                multipliedAnswer = firstNum * secondNum
                print("Found two numbers summing to 2020. First, " + str(firstNum) + ", Second, " + str(secondNum) + ", Multiplied, " + str(multipliedAnswer))
                found2020Pair = True
                break

        if found2020Pair:
            break

    if found2020Pair:
        print("Successfully found a pair!")
    else:
        print("Failed to find pair")

# MAIN
fileExpenses = readExpensesFile(expenseFileName)

partOneFind2NumbersThatSum(2020, fileExpenses)

