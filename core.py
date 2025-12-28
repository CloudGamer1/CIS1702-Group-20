from MapLogic import *

MapSave=LoadMap("Game-Map.csv")
TreasureData=LoadTresureData()

PlayerLocation=[2,2]

print(DisplayMap(PlayerLocation, MapSave))
RoomDescription(PlayerLocation, MapSave)