import csv
import json
import colorama
from colorama import Fore, Style


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
    rows = len(MapSave) 
    columns = len(MapSave[0]) 
    DisplayMap = [] 
    
    for r in range(rows): 
        for c in range(columns): 
            
            if [r, c] == PlayerLocation: 
                DisplayMap.append("  x  ") 
                continue
             
            tile = MapSave[r][c] 

            if tile == "wall": 
                DisplayMap.append("-----") 
            elif tile[:4] == "door": 
                DisplayMap.append(" [ ] ") 
            elif tile[:4] == "Npc1": 
                DisplayMap.append(" 0-0 ")
            elif tile[:4] == "Npc2": 
                DisplayMap.append(f" {Fore.GREEN}0V0{Style.RESET_ALL} ")
            else: 
                DisplayMap.append("     ")
            
        DisplayMap.append("\n") 
    
    
    return "".join(DisplayMap)



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

def LoadNpcData():
    '''Loads Npc Data from a JSON file'''
    try:
        with open("Npc.json","r") as NpcFile:
            NpcData=json.load(NpcFile)
    except FileNotFoundError:
        print("Npc file not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from Npc file")
    
    return NpcData

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

def LoadDoorData():
    '''Loads Door Data from a JSON file'''
    try:
        with open("Doors.json","r") as DoorsFile:
            DoorsData=json.load(DoorsFile)
    except FileNotFoundError:
        print("Doors file not found")
    except json.JSONDecodeError:
        print("Error decoding JSON from Doors file")
    
    return DoorsData

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

def UseDoor(PlayerLocation, MapSave, DoorData, lastcommand, NpcLocations):
    '''Uses a door to move to another location'''
    door=MapSave[PlayerLocation[0]][PlayerLocation[1]]
    for doorId in DoorData:
        if doorId.lower() == door.lower():
            if lastcommand=="w":
                PlayerLocation[0]+=1
            elif lastcommand=="s":
                PlayerLocation[0]-=1
            elif lastcommand=="a":
                PlayerLocation[1]-=1
            elif lastcommand=="d":
                PlayerLocation[1]+=1
            
            if PlayerLocation == DoorData[doorId]['Location1']:
                origin = DoorData[doorId]['Location1']
                PlayerLocation=DoorData[doorId]['Location2']   
            elif PlayerLocation == DoorData[doorId]['Location2']:
                origin = DoorData[doorId]['Location2']
                PlayerLocation=DoorData[doorId]['Location1']
            else:
                print("Error using door")
                return PlayerLocation
        
        for npc, info in NpcLocations.items(): #if npc blocks the door
            if info["pos"] == PlayerLocation: 
                print("Someone is standing here! You are pushed back through the door.") 
                return origin
        
    return PlayerLocation
    
def UpdateDoorFile():
    
    DoorData={
        "Door1":{
            "Location1":[5,1],
            "Location2":[7,1],
            "Locked":False #we cann add locking mechanics later
        },
        "Door2":{
            "Location1":[1,1],
            "Location2":[4,4],
            "Locked":True
        }
    }
    
    '''Updates the door data file'''
    try:
        with open("Doors.json","w") as DoorsFile:
            json.dump(DoorData,DoorsFile,indent=4)
    except IOError:
        print("Error writing to Doors file")

