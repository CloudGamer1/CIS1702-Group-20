from MapLogic import *
from PlayerLogic import *

MapSave=LoadMap("Game-Map.csv")
print(MapSave[1][2])
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

    print(DisplayMap(PlayerLocation, MapSave))