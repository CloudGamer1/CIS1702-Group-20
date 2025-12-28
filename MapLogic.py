import csv

def LoadMap(MapFileName):
    '''Loads Map From a CSV files'''
    
    MapFileName=MapFileName

    try:
        with open(MapFileName,"r") as MapFile:
            Reader=csv.reader(MapFile)
            Map=[]
            for row in Reader:
                Map.append(row)
        return Map
    except FileNotFoundError:
        print("Map file not found")

def DisplayMap(PlayerLocation, MapFileName):
    '''Displays the map and the current player position'''
    MapSave=LoadMap(MapFileName)
    CurrentLocation=[0,0]
    DisplayMap=[]
    try:
        RowLenght=len(MapSave[0])
    except IndexError:
        print("Map is empty")

    for I in MapSave:
        location=0
        for J in I:
            location+=1
            if CurrentLocation==PlayerLocation:
                DisplayMap.append("  x  ")
            elif J == "wall":
                DisplayMap.append("-----")
            elif J != "wall" or J != "door":
                DisplayMap.append("     ")
            
            if location >= RowLenght:
                DisplayMap.append("\n")
            CurrentLocation[1]=CurrentLocation[1]+1
        CurrentLocation[0]=CurrentLocation[0]+1
        CurrentLocation[1]=0
    return (" ".join(DisplayMap))
