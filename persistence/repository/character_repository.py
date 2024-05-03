from typing import Any, List, Tuple
from dataclasses import dataclass


from infra.db import *
from model.character import Character
from model.classe import Classe
from model.user import User
from persistence.interface.character_interface import CharacterInterface

@dataclass
class characterDTO:
    name: str
    _class: Classe
    user: User
    level: int
    health: int
    exp: int
    damage: int
    
class CharacterRepository(CharacterInterface):
    def __init__(self):
        conn, cursor = get_db()

        cursor.execute('''CREATE TABLE IF NOT EXISTS personagens
                  (nome TEXT PRIMARY KEY, 
                  classe TEXT, 
                  user_username TEXT,
                  level INTEGER,
                  health INTEGER,
                  exp INTEGER,
                  damage INTEGER,
                  FOREIGN KEY(user_username) REFERENCES user(username),
                  FOREIGN KEY(classe) REFERENCES classes(classe))''')

        conn.commit()
        
    def insertCharacter(self, character: Character, user: User):

        conn, cursor = get_db()
        
        try:
            statement = "SELECT * FROM personagens WHERE nome = ?", (character.name,)
            cursor.execute(statement)
            query = cursor.fetchone()
            
            if query:
                print("Já existe personagem com esse nome.")
                return None
            
            statement = """INSERT INTO personagens (
                        nome,
                        classe, 
                        user_username, 
                        level,
                        health,
                        exp,
                        damage) VALUES 
                        (?, ?, ?, ?, ?, ?, ?)""", (character.name, character._class, user.username, character.level, character.health, character.exp, character.damage)
            
            cursor.execute(statement)
            conn.commit()
            
            return character
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
    
    def deleteUserCharacter(self, character: Character):
        conn, cursor = get_db()
        
        try:
            statement = "DELETE FROM personagens WHERE character = ?", (character.character,)
            cursor.execute(statement)
            conn.commit()
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
            
    def getUserCharacters(self,  userRef : User):
        conn, cursor = get_db()
        print(f'repo char: {userRef.username}')
        try:
            statement = f"""SELECT * FROM personagens WHERE user_username = {userRef.username};"""
            cursor.execute(statement)
            query = cursor.fetchall()
            print(f'query repo char: {query}')
            if not query:
                return None
                
            return [characterDTO(q[0], q[1], q[2], q[3], q[4], q[5], q[6]) for q in query]
        
        except Exception as e:
            print(e)
        
        finally:
            close_db(conn)
            
        