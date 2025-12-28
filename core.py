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
        PlayerLocation=MoveUp(PlayerLocation)
    elif command == "s":
        PlayerLocation=MoveDown(PlayerLocation)
    elif command == "a":
        PlayerLocation=MoveLeft(PlayerLocation)
    elif command == "d":
        PlayerLocation=MoveRight(PlayerLocation)

    print(DisplayMap(PlayerLocation, MapSave))