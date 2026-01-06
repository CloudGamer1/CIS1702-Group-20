class Player():
    def __init__(self): # Initiallises the player class with a starting position and health
        self.Player_Health = 100
        self.Player_Max_Health = 100
        self.PlayerLocation = [1,1]

    def MoveUp(self,map):
        '''Moves the player up one space on the map'''
        
        self.PlayerLocation[0]-=1

        if map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "wall":
            self.CollideWall("Up") # Displays a message when colliding and places back to where the character was already
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc1":
            self.CollideNpc("Npc1","Up") # Displays a message when colliding with an npc and places back to where the character was already
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc2":
            self.CollideNpc("Npc2","Up") 
        return self.PlayerLocation

    def MoveDown(self,map):
        '''Moves the player down one space on the map'''
        
        self.PlayerLocation[0]+=1

        if map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "wall":
            self.CollideWall("Down") 
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc1":
            self.CollideNpc("Npc1","Down")
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc2":
            self.CollideNpc("Npc2","Down")
        return self.PlayerLocation

    def MoveLeft(self,map):
        '''Moves the player left one space on the map'''
        
        self.PlayerLocation[1]-=1

        if map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "wall":
            self.CollideWall("Left")
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc1":
            self.CollideNpc("Npc1","Left")
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc2":
            self.CollideNpc("Npc2","Left")
        return self.PlayerLocation

    def MoveRight(self,map):
        '''Moves the player right one space on the map'''
        
        self.PlayerLocation[1]+=1

        if map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "wall":
            self.CollideWall("Right")
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc1":
            self.CollideNpc("Npc1","Right")
        elif map[self.PlayerLocation[0]][self.PlayerLocation[1]] == "Npc2":
            self.CollideNpc("Npc2","Right")
        return self.PlayerLocation
    
    def CollideNpc(self,Npc,Movement_Angle):
        if Npc == "Npc1":
            if Movement_Angle == "Up": # Direction being moved
                print("Heres a Nutritious Meal!") # Message to show what happens when touching npc
                self.Player_Health += 10 # Heals the player 10 health
                if self.Player_Health > self.Player_Max_Health: # Ensures the player doesnt go above its max health
                    self.Player_Health = self.Player_Max_Health
                self.Collide(Movement_Angle) # Collision detection
            if Movement_Angle == "Left":
                print("Heres a Nutritious Meal!")
                self.Player_Health += 10
                if self.Player_Health > self.Player_Max_Health:
                    self.Player_Health = self.Player_Max_Health
                self.Collide(Movement_Angle)
            if Movement_Angle == "Down":
                print("Heres a Nutritious Meal!")
                self.Player_Health += 10
                if self.Player_Health > self.Player_Max_Health:
                    self.Player_Health = self.Player_Max_Health
                self.Collide(Movement_Angle)
            if Movement_Angle == "Right":
                print("Heres a Nutritious Meal!")
                self.Player_Health += 10
                if self.Player_Health > self.Player_Max_Health:
                    self.Player_Health = self.Player_Max_Health
                self.Collide(Movement_Angle)
        if Npc == "Npc2":
            if Movement_Angle == "Up":
                print("You were attacked by a Goblin!")
                self.Collide(Movement_Angle)
        if Movement_Angle == "Left":
                print("You were attacked by a Goblin!")
                self.Collide(Movement_Angle)
        if Movement_Angle == "Down":
                print("You were attacked by a Goblin!")
                self.Collide(Movement_Angle)
        if Movement_Angle == "Right":
                print("You were attacked by a Goblin!")
                self.Collide(Movement_Angle)

    def CollideWall(self,Movement_Angle):
        if Movement_Angle == "Up":
            print("You hit a wall! Can't move up.") # Displays a message showing why the player cant move
            self.Collide(Movement_Angle) # Collision detection
        if Movement_Angle == "Left":
            print("You hit a wall! Can't move left.")
            self.Collide(Movement_Angle)
        if Movement_Angle == "Down":
            print("You hit a wall! Can't move down.")
            self.Collide(Movement_Angle)
        if Movement_Angle == "Right":
            print("You hit a wall! Can't move right.")
            self.Collide(Movement_Angle)
        
    def Collide(self,Movement_Angle):
        if Movement_Angle == "Up": 
            self.PlayerLocation[0]+=1 # Moves player back down 1 place in the y axis
            return self.PlayerLocation
        if Movement_Angle == "Left":
            self.PlayerLocation[1]+=1 # Moves player back down 1 place in the x axis
            return self.PlayerLocation
        if Movement_Angle == "Down":
            self.PlayerLocation[0]-=1
            return self.PlayerLocation
        if Movement_Angle == "Right":
            self.PlayerLocation[1]-=1
            return self.PlayerLocation



