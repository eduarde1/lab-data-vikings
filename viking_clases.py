# Soldier

class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    def attack(self):
        return self.strength
    def receive_damage(self, damage): 
        self.health -= damage
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        self.name = name
        super().__init__(health, strength)
    def receive_damage(self, damage): 
        self.health -= damage
        if self.health > 0:
            return f'{self.name} has received {damage} points of damage'
        else:
            return f'{self.name} has died in act of combat'
    def battle_cry(self):
        return 'Odin Owns You All!'
   



# Saxon
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)
    def receive_damage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f'A Saxon has received {damage} points of damage'
        else:
            return 'A Saxon has died in combat'
    
    

# War

import random
class War:
    def __init__(self):
        self.saxon_army = []
        self.viking_army = []
    def add_viking(self, Viking):
        self.viking_army.append(Viking)    
    def add_saxon(self, Saxon):
        self.saxon_army.append(Saxon)
    def viking_attack(self):
        Saxon.receive_damage = strength(Viking)          
        if Saxon.health <= 0:
            self.viking_army.pop(Saxon)          
        return Saxon.receive_damage
    def saxon_attack(self):
        Viking.receive_damage == random(0, len(self.viking_army)-1)
        if Viking.health <= 0:
            self.viking_army.pop(Viking)
        return Viking.receive_damage
    def show_status(self):
        if self.saxon_army == []:
            return 'Saxons have fought for their lives and survive another day...'
        elif self.viking_army == []:
            return 'Saxons have fought for their lives and survive another day...'
        elif self.saxon_army == [Saxon[1]] and self.viking_army == [Viking[1]]:
            return 'Vikings and Saxons are still in the thick of battle.'
    

