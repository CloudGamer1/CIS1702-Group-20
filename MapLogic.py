import csv
import json

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

def DisplayMap(PlayerLocation, MapSave):
    '''Displays the map and the current player position'''
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

def LoadRoomData():
    '''Loads Room Data from a JSON file'''
    try:
        with open("Rooms.json","r") as RoomsFile:
            RoomsData=json.load(RoomsFile)
    except FileNotFoundError:
        print("Rooms file not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from Rooms file")
    return RoomsData

def LoadTresureData():
    '''Loads Tresure Data from a JSON file'''
    try:
        with open("Tresures.json","r") as TresureFile:
            TresuresData=json.load(TresureFile)
    except FileNotFoundError:
        print("Tresure file not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from Tresure file")
    
    return TresuresData

def GiveTreasure(TreasuresData,TreasureID):
    '''Gives the player the treasure'''
    
    for tresure in TreasuresData:
        if TreasureID.lower() == tresure.lower():
            print(f"You have found a {TreasuresData[tresure]['Tresure']}!")
            return TreasuresData[tresure]['Tresure']
        print("error finding treasure")

def RoomDescription(PlayerLocation, MapSave):
    '''Returns the description of the room the player is in'''
    
    RoomsData=LoadRoomData()

    try:
        roomdata=MapSave[PlayerLocation[0]][PlayerLocation[1]]
    except IndexError:
        print("Player location is out of map bounds")
        return

    if roomdata[:8].lower() == "treasure":
        TreasuresData=LoadTresureData()
        for tresure in TreasuresData:
            if roomdata.lower() == tresure.lower():
                roomdata=TreasuresData[tresure]['RoomType'].lower()
        
    for room in RoomsData:
        if roomdata.lower() == room.lower():
            data=[RoomsData[room]['Name'],RoomsData[room]['Description']]
            return data
    print("You are in an undefined area")

