from MapLogic import *
from PlayerLogic import *

MapSave=LoadMap("Game-Map.csv")
TreasureData=LoadTresureData()

PlayerLocation=[1,1]

#print(MoveUp(PlayerLocation))

print(DisplayMap(PlayerLocation, MapSave))
#RoomDescription(PlayerLocation, MapSave)

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
        print(f"You found treasure: {treasure}")
        #when player inventory gets added add the treasure to inventory here
    
    print(DisplayMap(PlayerLocation, MapSave))