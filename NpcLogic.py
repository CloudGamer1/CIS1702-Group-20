import random

def MoveNpc(Npc_name, NpcLocations, MapSave, NpcData, PlayerLocation):
    x, y = NpcLocations[Npc_name]["pos"]
    under = NpcLocations[Npc_name]["under"]


    direction = random.choice(["w", "a", "s", "d"])
    
    new_x, new_y = x, y
    if direction == "w": new_x -= 1
    elif direction == "s": new_x += 1
    elif direction == "a": new_y -= 1
    elif direction == "d": new_y += 1
    
    if [new_x, new_y] == PlayerLocation: 
        return
    
    tile = MapSave[new_x][new_y].lower()
    
    # Npcs cannot walk through walls or other NPCs 
    if tile == "wall" or tile.startswith("npc") or tile.startswith("door"): 
        return 
    
    MapSave[x][y] = under 
    NpcLocations[Npc_name]["under"] = MapSave[new_x][new_y]

    MapSave[new_x][new_y] = Npc_name
    NpcLocations[Npc_name]["pos"] = [new_x, new_y]
