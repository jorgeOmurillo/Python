textFile = open("maze2.txt", 'r')

def drawMe(textFile):
    mazeList = []
    rowsInMaze = 0
    columnsInMaze = 0

    for x in textFile:
        rows = []
        columns = 0

        for y in x[:-1]:
            rows.append(y)

            if y == 'S':
                startRow = rowsInMaze
                startCol = columns

            columns += 1
        
        rowsInMaze += 1
        mazeList.append(rows)
        columnsInMaze = len(rows)

print "me"
