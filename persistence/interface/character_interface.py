from typing import List, Tuple
from abc import ABC, abstractmethod

from model.character import Character
from model.classe import Classe
from model.user import User

class CharacterInterface(ABC):
    
    @abstractmethod
    def insertCharacter(self, character: Character, user : User):
        raise NotImplementedError

    @abstractmethod
    def deleteUserCharacter(self, char : Character):
        raise NotImplementedError
    
    @abstractmethod
    def getUserCharacters(self, user : User):
        raise NotImplementedError

    

