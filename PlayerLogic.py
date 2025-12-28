def MoveUp(PlayerLocation,map):
    '''Moves the player up one space on the map'''
    
    PlayerLocation[0]-=1
    if map[PlayerLocation[0]][PlayerLocation[1]] == "wall":
        print("You hit a wall! Can't move up.")
        PlayerLocation[0]+=1
        return PlayerLocation
    return PlayerLocation

def MoveDown(PlayerLocation,map):
    '''Moves the player down one space on the map'''
    
    PlayerLocation[0]+=1
    if map[PlayerLocation[0]][PlayerLocation[1]] == "wall":
        print("You hit a wall! Can't move down.")
        PlayerLocation[0]-=1
        return PlayerLocation
    return PlayerLocation

def MoveLeft(PlayerLocation,map):
    '''Moves the player left one space on the map'''
    
    PlayerLocation[1]-=1
    if map[PlayerLocation[0]][PlayerLocation[1]] == "wall":
        print("You hit a wall! Can't move left.")
        PlayerLocation[1]+=1
        return PlayerLocation
    return PlayerLocation

def MoveRight(PlayerLocation,map):
    '''Moves the player right one space on the map'''
    
    PlayerLocation[1]+=1
    if map[PlayerLocation[0]][PlayerLocation[1]] == "wall":
        print("You hit a wall! Can't move right.")
        PlayerLocation[1]-=1
        return PlayerLocation
    return PlayerLocation