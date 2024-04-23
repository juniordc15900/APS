

from typing import List
from model.character import Character
from model.user import User
from persistence.interface.character_interface import CharacterInterface
from persistence.repository.character_repository import CharacterRepository


class characterUseCase:
    
    def __init__(self,
                 character_repository: CharacterInterface):
        
        self.character_repository = character_repository

    def getAllcharacters(self, user: User) -> List[Character]:
        print(f'usecase char:{user.username}')
        character_get = self.character_repository.getUserCharacters(user)
        print(f'char use case list {character_get}')
        if not character_get:
            return None
        
        return [Character(character.name,character._class, character.user, character.level, character.health, character.exp, character.damage) for character in character_get]
        
    def createUserCharacter(self, character: Character) -> Character:
    
        character_insert = self.character_repository.insertCharacter(character)
        return character_insert
    
    def deleteUserCharacter(self, character: Character):
        
        self.character_repository.deletecharacter(character)
    