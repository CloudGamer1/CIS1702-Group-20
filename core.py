from MapLogic import *
from PlayerLogic import *
from NpcLogic import *

MapSave = LoadMap("Game-Map.csv")
player = Player()
Npcs = []
TreasureData = LoadTresureData()
DoorData = LoadDoorData()

Npcs = []
NpcData = LoadNpcData()
for i in NpcData:
    Npcs.append(Npc(i))


NpcLocations = {}
player.PlayerLocation = [1, 1]

for Npc_name, Npc_info in NpcData.items():
    if "Location1" in Npc_info:
        x, y = Npc_info["Location1"]

        NpcLocations[Npc_name] = {"pos": [x, y], "under": MapSave[x][y]}
        MapSave[x][y] = Npc_name


print(DisplayMap(player.PlayerLocation, MapSave))

with open("WinCondition.json", "r") as WinCondition_file:
    WinCondition = json.load(WinCondition_file)


while True:
    for NameNpcs in Npcs:
        if NameNpcs.Npc_Alive == False:
            MapSave[NameNpcs.NpcPosition[0]][
                NameNpcs.NpcPosition[1]
            ] = NameNpcs.RoomType
            if NameNpcs.name == WinCondition["Winning_Npc"]:
                print(WinCondition["Winning_Message"])
                exit()

    Used_door = False
    command = input("\n")
    player.Move(command, MapSave)

    if (
        MapSave[player.PlayerLocation[0]][player.PlayerLocation[1]][:4].lower()
        == "door"
    ):
        player.PlayerLocation = UseDoor(
            player.PlayerLocation, MapSave, DoorData, command, NpcLocations
        )
        used_door = True

    if not Used_door:  # Npc move only if the player did not use the door
        for npc in NpcLocations:
            Npc.MoveNpc(npc, NpcLocations, MapSave, NpcData, player.PlayerLocation)

    if (
        MapSave[player.PlayerLocation[0]][player.PlayerLocation[1]][:8].lower()
        == "treasure"
    ):
        print("You found a treasure!")
        treasure = GiveTreasure(
            TreasureData, MapSave[player.PlayerLocation[0]][player.PlayerLocation[1]]
        )
        # when player inventory gets added add the treasure to inventory here
        RoomType = RoomDescription(player.PlayerLocation, MapSave)[0]
        MapSave[player.PlayerLocation[0]][player.PlayerLocation[1]] = RoomType
    elif (
        MapSave[player.PlayerLocation[0]][player.PlayerLocation[1]][:4].lower()
        == "door"
    ):
        player.PlayerLocation = UseDoor(
            player.PlayerLocation, MapSave, DoorData, command
        )
        print(f"You are now in {RoomDescription(player.PlayerLocation, MapSave)[0]}")

    print(DisplayMap(player.PlayerLocation, MapSave))
