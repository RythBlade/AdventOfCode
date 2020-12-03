
class Map:
    def __init__(self, mapFile):
        self.__map = mapFile

        # clean up the white space characters - they're not part of the map data
        for lineIdx in range(self.getMapHeight()):
            self.__map[lineIdx] = self.__map[lineIdx].strip()

    def isSlotATree(self, x, y):
        return self.__isMapCellCharacter('#', x, y)

    def isSlotOpen(self, x, y):
        return self.__isMapCellCharacter('.', x, y)

    def __isMapCellCharacter(self, character, x, y): # python doesn't support public/private - but convention is that things with '__' are private
        localWidth = self.getMapWidth()
        localHeight = self.getMapHeight()

        if localWidth > 0 and y < localHeight:
            xLocalIndex = x % localWidth
            yLocalIndex = y

            if self.__map[yLocalIndex][xLocalIndex] == character:
                return True
            else:
                return False
        else:
            return False

    def getMapHeight(self):
        return len(self.__map)

    def getMapWidth(self):
        if self.getMapHeight() > 0:
            return len(self.__map[0])
        else:
            return 0