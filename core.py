from MapLogic import *
from PlayerLogic import *

MapSave=LoadMap("Game-Map.csv")
TreasureData=LoadTresureData()
DoorData=LoadDoorData()

PlayerLocation=[1,1]

print(DisplayMap(PlayerLocation, MapSave))


while True:
    command=input("\n")
    if command == "w":
        PlayerLocation=MoveUp(PlayerLocation,MapSave)
    elif command == "s":
        PlayerLocation=MoveDown(PlayerLocation,MapSave)
    elif command == "a":
        PlayerLocation=MoveLeft(PlayerLocation,MapSave)
    elif command == "d":
        PlayerLocation=MoveRight(PlayerLocation,MapSave)

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