from model.classe import Classe
from model.user import User
import random

class Character:
    
    def __init__(self, name, _class: Classe, user : User, level=None, health=None, exp=None, damage=None):
        self.name = name
        self._class = _class
        self.user = user
        self.level = level if level else 0
        self.health = health if health else 0
        self.exp = exp if exp else 0
        self.damage = damage if damage else 0
    
    def __str__(self):
        return f"User: {self.user}, Name: {self.name}, Classe: {self._class}, Level: {self.level}, Health: {self.health}, Damage: {self.damage}, Exp: {self.exp}"
        