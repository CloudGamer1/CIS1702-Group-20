import csv

def LoadMap():
    '''Loads Map From a CSV files'''
    MapFileName="Game-Map.csv"

    with open(MapFileName,"r") as MapFile:
        Reader=csv.reader(MapFile)
        Map=[]
        for row in Reader:
            Map.append(row)
    return Map


def DisplayMap():
    '''Displays the map and the current player position'''
    MapSave=LoadMap()

    DisplayMap=[]
    RowLenght=len(MapSave[0])

    for I in MapSave:
        location=0
        for J in I:
            location+=1
            if J == "wall":
                DisplayMap.append("----")
            elif J != "wall" or J != "door":
                DisplayMap.append("    ")
            if location >= RowLenght:
                DisplayMap.append("\n")
            
    return (" ".join(DisplayMap))
    
    
