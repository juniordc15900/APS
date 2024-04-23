from model.classe import Classe
from model.user import User
import random

class Character:
    
    def __init__(self, name, _class: Classe, user : User):
        self.name = name
        self._class = _class
        self.user = user
        self.level = 0
        self.health = 10
        self.exp = 0
        self.damage = 0
    
    def __str__(self):
        return f"User: {self.user}, Name: {self.name}, Classe: {self._class}, Level: {self.level}, Health: {self.health}, Damage: {self.damage}, Exp: {self.exp}"
        