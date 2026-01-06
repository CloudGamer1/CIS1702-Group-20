import random
from PlayerLogic import *

class Npc:
    def __init__(self, name, NpcPos, MapSave, item,RoomType, Hostile, Npc_Health, Npc_Health_Max):
        self.name = name
        self.NpcPosition = NpcPos
        self.item = item
        self.RoomType = RoomType
        self.Hostile = Hostile
        self.Npc_Health = Npc_Health
        self.Npc_Health_Max = Npc_Health_Max
        self.Npc_Alive = True
        self.tile = MapSave[self.NpcPosition[0]][self.NpcPosition[1]].lower()

    def MoveNpc(self, NpcPosition, MapSave, PlayerLocation):
        direction = random.choice(["Up", "Down", "Left", "Right"])
        if direction == "Up":
            self.NpcPosition[0]-=1
            if MapSave[self.NpcPosition[0]][self.NpcPosition[1]] == "wall":
                if self.Npc_Alive == True:
                    self.CollideWall(direction,PlayerLocation)
        elif direction == "Down":
            self.NpcPosition[0]+=1
            if MapSave[self.NpcPosition[0]][self.NpcPosition[1]] == "wall":
                if self.Npc_Alive == True:
                    self.CollideWall(direction,PlayerLocation)
        elif direction == "Left":
            self.NpcPosition[1]-=1
            if MapSave[self.NpcPosition[0]][self.NpcPosition[1]] == "wall":
                if self.Npc_Alive == True:
                 self.CollideWall(direction,PlayerLocation)
        elif direction == "Right":
            self.NpcPosition[1]+=1 
            if MapSave[self.NpcPosition[0]][self.NpcPosition[1]] == "wall":
                if self.Npc_Alive == True:
                    self.CollideWall(direction,PlayerLocation)
        self.tile = MapSave[self.NpcPosition[0]][self.NpcPosition[1]].lower()

    def CollideWall(self,Movement_Angle,PlayerLocation):
            if Movement_Angle == "Up":
                self.Collide(Movement_Angle) # Collision detection
            if Movement_Angle == "Left":
                self.Collide(Movement_Angle)
            if Movement_Angle == "Down":
                self.Collide(Movement_Angle)
            if Movement_Angle == "Right":
                self.Collide(Movement_Angle)
            if tile.startswith("door"):
                return  # Npcs do not interact with doors
            if [self.NpcPosition[0]][self.NpcPosition[1]] == PlayerLocation:
                if self.Hostile:
                    self.DamageNpc(random.randint(5, 15))  # Player attacks Npc on collision
                return
        
    def Collide(self,Movement_Angle):
        if Movement_Angle == "Up": 
            self.NpcLocation[0]+=1 # Moves npc back down 1 place in the y axis
            return self.NpcLocation
        if Movement_Angle == "Left":
            self.NpcLocation[1]+=1 # Moves npc back down 1 place in the x axis               
            return self.NpcLocation
        if Movement_Angle == "Down":
            self.NpcLocation[0]-=1
            return self.NpcLocation
        if Movement_Angle == "Right":
            self.NpcLocation[1]-=1
            return self.NpcLocation
        
    def DamageNpc(self, damage): # Reduces the npc's health by the specified damage amount
        self.Npc_Health -= damage
        if self.Npc_Health < 0:
            self.Npc_Health = 0
        elif self.Npc_Health <= 0:
            self.Npc_Alive = False

        