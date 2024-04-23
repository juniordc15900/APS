from model.character import Character
from model.user import User
from persistence.database import Database
import random

class Controler():
    def __init__(self, db : Database):
        self.db = db
        pass
    
    def userLogin(self, username, password):
        userL  =  self.db.searchUser( User(username, password) )
        return userL

    def userRegister(self, username, password):
        userL  =  self.db.insertUser(User(username, password))
        return userL

    def deleteUser(self, username, password):
        self.db.deleteUser( User(username, password) )

    def getAllowedClasses(self):
        return self.db.classes

    def createUserCharacter(self, name , _class, user : User):
        char  = self.db.insertCharacter( Character(name, _class, user), user )
        return char

    def getUserCharacters(self, user : User):
        chars = self.db.getUserCharacters(user)
        charsObj = [Character( char[0], char[1], user) for char in chars ]
        return charsObj

    def deleteUserCharacter(self, char : Character, user : User):
        self.db.deleteCharacter(char)