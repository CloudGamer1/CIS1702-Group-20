from MapLogic import *
from PlayerLogic import *
from NpcLogic import*

MapSave=LoadMap("Game-Map.csv")
TreasureData=LoadTresureData()
DoorData=LoadDoorData()
NpcData=LoadNpcData()
NpcLocations = {}
PlayerLocation=[1,1]

for Npc_name, Npc_info in NpcData.items():
    if "Location1" in Npc_info:
        x, y = Npc_info["Location1"]

        NpcLocations[Npc_name] = {
            "pos": [x, y],
            "under": MapSave[x][y]
        }
        MapSave[x][y] = Npc_name


print(DisplayMap(PlayerLocation, MapSave))


while True:
    Used_door = False
    command=input("\n")
    if command == "w":
        PlayerLocation=MoveUp(PlayerLocation,MapSave)
    elif command == "s":
        PlayerLocation=MoveDown(PlayerLocation,MapSave)
    elif command == "a":
        PlayerLocation=MoveLeft(PlayerLocation,MapSave)
    elif command == "d":
        PlayerLocation=MoveRight(PlayerLocation,MapSave)
        

    if MapSave[PlayerLocation[0]][PlayerLocation[1]][:4].lower() == "door": 
        PlayerLocation = UseDoor(PlayerLocation, MapSave, DoorData, command, NpcLocations)  
        used_door = True 
    
    
    if not Used_door: #Npc move only if the player did not use the door
        for npc in NpcLocations: 
            MoveNpc(npc, NpcLocations, MapSave, NpcData, PlayerLocation)

    if MapSave[PlayerLocation[0]][PlayerLocation[1]][:8].lower() == "treasure":
        print("You found a treasure!")
        treasure=GiveTreasure(TreasureData,MapSave[PlayerLocation[0]][PlayerLocation[1]])
        #when player inventory gets added add the treasure to inventory here
        RoomType=RoomDescription(PlayerLocation, MapSave)[0]
        MapSave[PlayerLocation[0]][PlayerLocation[1]]=RoomType
    elif MapSave[PlayerLocation[0]][PlayerLocation[1]][:4].lower() == "door":
        PlayerLocation=UseDoor(PlayerLocation, MapSave, DoorData,command)    
        print(f"You are now in {RoomDescription(PlayerLocation, MapSave)[0]}")
        
        
        
    print(DisplayMap(PlayerLocation, MapSave))