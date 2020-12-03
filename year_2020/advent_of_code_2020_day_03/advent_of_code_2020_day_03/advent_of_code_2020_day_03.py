
from Timer import Timer
from Map import Map

mapFilename = "tree_map.txt"

def loadMapFile(filename):
    with open(filename) as file:
        lines = file.readlines()
        return lines

def part1TreesEncountered(map, startX, startY, xStep, yStep):
    treesEncountered = 0
    mapHeight = map.getMapHeight()

    xTestPos = startX
    yTestPos = startY

    while yTestPos < mapHeight:
        isTree = map.isSlotATree(xTestPos, yTestPos)

        if isTree:
            treesEncountered += 1

        xTestPos += xStep
        yTestPos += yStep

    return treesEncountered

applicationTimer = Timer()

print("Application started")

map = Map(loadMapFile(mapFilename))

print("Map file read, " + mapFilename)

#############################################
treesEncounteredPart1 = part1TreesEncountered(map, 0, 0, 3, 1)
print("Part 1. Trees encountered, " + str(treesEncounteredPart1))
#############################################

#############################################
treesMultipliedTogetherForPart2 = part1TreesEncountered(map, 0, 0, 1, 1)
treesMultipliedTogetherForPart2 *= part1TreesEncountered(map, 0, 0, 3, 1)
treesMultipliedTogetherForPart2 *= part1TreesEncountered(map, 0, 0, 5, 1)
treesMultipliedTogetherForPart2 *= part1TreesEncountered(map, 0, 0, 7, 1)
treesMultipliedTogetherForPart2 *= part1TreesEncountered(map, 0, 0, 1, 2)

print("Part 2. Trees multiplied together, " + str(treesMultipliedTogetherForPart2))
#############################################

print("Application completed. Time taken (s), " + str(applicationTimer.elapsedTime()))