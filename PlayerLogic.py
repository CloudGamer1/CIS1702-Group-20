def MoveUp(PlayerLocation):
    '''Moves the player up one space on the map'''
    
    PlayerLocation[0]-=1
    return PlayerLocation

def MoveDown(PlayerLocation):
    '''Moves the player down one space on the map'''
    
    PlayerLocation[0]+=1
    return PlayerLocation

def MoveLeft(PlayerLocation):
    '''Moves the player left one space on the map'''
    
    PlayerLocation[1]-=1
    return PlayerLocation

def MoveRight(PlayerLocation):
    '''Moves the player right one space on the map'''
    
    PlayerLocation[1]+=1
    return PlayerLocation