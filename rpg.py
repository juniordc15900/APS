from model.user import User
from model.character import Character
from persistence.database import Database
from control.controler import Controler
from view.view import App


db = Database()
controler = Controler(db)
app = App(controler)
app.mainloop()