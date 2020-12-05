
def binaryChopRange(sideMarkerList, frontHalfMarker, backHalfMarker, inclusiveMin, exclusiveMax):
    localMin = inclusiveMin
    localMax = exclusiveMax

    for marker in sideMarkerList:
        midpoint = localMin + ((localMax - localMin) // 2) # integer devision to find the min

        if marker == frontHalfMarker:
            localMax = midpoint
        elif marker == backHalfMarker:
            localMin = midpoint
        else:
            return -1

    return localMin + ((localMax - localMin) // 2)

def calculateSeatId(row, column):
    return row * 8 + column

class BoardingPass:

    def __init__(self, passString, numberOfRows, numberOfColumns):
        self.__passString = passString.strip()

        if len(self.__passString) != 10:
            self.row = -1
            self.column = -1
            self.seatID = -1
        else:
            self.row = binaryChopRange(self.__passString[:7], 'F', 'B', 0, numberOfRows)
            self.column = binaryChopRange(self.__passString[7:], 'L', 'R', 0, numberOfColumns)
            self.seatID = calculateSeatId(self.row, self.column)