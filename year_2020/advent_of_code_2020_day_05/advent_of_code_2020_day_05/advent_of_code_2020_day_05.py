from Timer import Timer
from BoardingPass import BoardingPass
from BoardingPass import calculateSeatId


def loadBoardPassFile(filename):
    with open(filename) as file:
        return file.readlines()

applicationTimer = Timer()

print("Application started!")

numberOfRows = 128
numberOfColumns = 8

boardingPassFilename = "boarding_passes.txt"
boardingPassStringList = loadBoardPassFile(boardingPassFilename)

print("Loaded boarding pass strings, {0}".format(len(boardingPassStringList)))

boardingPasses = []

highestSeatingId = -1

# prepare a 2-d boolean array to track which seats are occupied to make searching for the empty seat easier
occupiedSeats = []
for row in range(numberOfRows):
    newRow = []
    
    for column in range(numberOfColumns):
        newRow.append(False)

    occupiedSeats.append(newRow)
        

for line in boardingPassStringList:
    newPass = BoardingPass(line, numberOfRows, numberOfColumns)
    
    if newPass.seatID == -1:
        print("Bad pass found, {0}".format(newPass._BoardingPass__passString))
        continue

    if newPass.seatID > highestSeatingId:
        highestSeatingId = newPass.seatID

    occupiedSeats[newPass.row][newPass.column] = True

    boardingPasses.append(newPass)


firstOccupiedRow = -1
firstOccupiedColumn = -1

rowCounter = 0
columnCounter = 0

while rowCounter < numberOfRows and firstOccupiedRow == -1 and firstOccupiedColumn == -1:
    columnCounter = 0
    while columnCounter < numberOfColumns and firstOccupiedRow == -1 and firstOccupiedColumn == -1:
        if occupiedSeats[rowCounter][columnCounter]:
            firstOccupiedRow = rowCounter
            firstOccupiedColumn = columnCounter

        columnCounter += 1
    rowCounter += 1
    
lastOccupiedRow = -1
lastOccupiedColumn = -1

rowCounter = numberOfRows - 1
columnCounter = numberOfColumns - 1

while rowCounter >= 0 and lastOccupiedRow == -1 and lastOccupiedColumn == -1:
    columnCounter = numberOfColumns - 1
    while columnCounter >= 0 and lastOccupiedRow == -1 and lastOccupiedColumn == -1:
        if occupiedSeats[rowCounter][columnCounter]:
            lastOccupiedRow = rowCounter
            lastOccupiedColumn = columnCounter

        columnCounter -= 1
    rowCounter -= 1

# one of the seats in range of occupied seats is empty - this is our seat :)

rowCounter = firstOccupiedRow
columnCounter = firstOccupiedColumn
foundEmptySeat = False

while rowCounter < (lastOccupiedRow + 1) and foundEmptySeat == False:
    columnCounter = firstOccupiedColumn
    while columnCounter < (lastOccupiedColumn + 1) and foundEmptySeat == False:
        if occupiedSeats[rowCounter][columnCounter] == False:
            print("Found our empty seat! Row, {0}, Column, {1}, Seat ID, {2}".format(rowCounter, columnCounter, calculateSeatId(rowCounter, columnCounter)))
            foundEmptySeat = True

        columnCounter += 1
    rowCounter += 1

if highestSeatingId == -1:
    print("Something went wrong - no high seat ID has been found")
else:
    print("Processed boarding passes. Highest Seat ID, {0}".format(highestSeatingId))

print("Application complete. Time taken(s), {0}".format(applicationTimer.elapsedTime()))