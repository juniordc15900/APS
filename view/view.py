import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from functools import partial
from control.controler import Controler
from control.use_case.character_usecase import characterUseCase
from control.use_case.classe_usecase import ClasseUseCase
from control.use_case.user_usecase import UserUseCase
from model.character import Character
from model.user import User
from persistence.interface.user_interface import UserInterface
from persistence.repository.character_repository import CharacterRepository
from persistence.repository.classe_repository import ClasseRepository
from persistence.repository.user_repository import UserRepository

def user_factory():
    user_repository = UserRepository()
    user_usecase = UserUseCase(user_repository)
    
    return user_usecase

def classe_factory():
	classe_repository = ClasseRepository()
	classe_usercase = ClasseUseCase(classe_repository)

	return classe_usercase

def character_factory():
	character_repository = CharacterRepository()
	character_usercase = characterUseCase(character_repository)

	return character_usercase

class App(tk.Tk):
	def __init__(self, controler : Controler):
		self.controler = controler

		super().__init__()
		self.title('Login')
		self.geometry('600x400')

		#====================================== Tela Login ==============================================
		self.login_frame = tk.Frame(self)
		ttk.Label(self.login_frame, text='Login', font=("Helvetica, 24")).pack(anchor="center", pady=10)
		ttk.Label(self.login_frame, text='Username*').pack(anchor="center", pady=10)
		ttk.Entry(self.login_frame).pack(anchor="center", pady=10)
		ttk.Label(self.login_frame, text='Password*').pack(anchor="center", pady=10)
		ttk.Entry(self.login_frame, ).pack(anchor="center", pady=10)
		button1 = ttk.Button(self.login_frame, text='Login', command = self.login)
		button1.pack(expand=True, anchor="center", pady=10)
		button2 = ttk.Button(self.login_frame, text='Registrar', command=self.register)
		button2.pack(expand=True, anchor="center", pady=10)
		button2 = ttk.Button(self.login_frame, text='Excluir Conta', command=self.deleteUser)
		button2.pack(expand=True, anchor="center", pady=10)
		
		#================Tela De criação de personagem=============================
		classe_usecase = classe_factory()
		self.createchar_frame = tk.Frame(self)
		ttk.Label(self.createchar_frame, text='Criar Personagem',font=("Helvetica, 24")).pack(anchor="center", pady=10)
		ttk.Label(self.createchar_frame, text='Nome*').pack(anchor="center")
		ttk.Entry(self.createchar_frame).pack(anchor="center", pady=10)
		ttk.Label(self.createchar_frame, text='Classe*').pack(anchor="center")
		combo = ttk.Combobox(self.createchar_frame)
		combo['values'] = [classe.classe for classe in classe_usecase.getAllClasses()]
		combo.current(1)
		combo.pack(anchor="center", pady=10)
		ttk.Button(self.createchar_frame, text='Criar', command= self.createChar).pack()

		#ttk.Button(self.createchar_frame, text='Criar', command=partial(self.back_to_main_menu, self.createchar_frame)).pack()




		
		#========== Tela que ira começar o programa ============
		self.login_frame.pack()



	#========================================Tela principal=======================================
	def drawMainScreen(self):
		self.main_frame = tk.Frame(self)
		ttk.Label(self.main_frame, text='Menu', font=("Helvetica, 24")).pack(anchor="center", pady=10)
		self.l_frame = tk.Frame(self.main_frame)
		self.l_frame.pack(fill="both", expand=True, side="left")
		self.r_frame = tk.Frame(self.main_frame)
		self.r_frame.pack(fill="both", expand=True, side="right")
		char_usecase = character_factory()
		chars = char_usecase.getAllcharacters(self.logged_user)
		if chars:
			for char in chars:
				char_frame = tk.Frame(self.l_frame)
				char_frame.pack(fill="both", expand=True)
				print(char)
				ttk.Label(char_frame, text=f'Nome: {char.name} |  Classe: {char._class}', width=40).pack(anchor="center", side="left", padx=(30, 0))
				ttk.Button(char_frame, text='Excluir', command= partial(self.deleteChar, char)).pack(expand=True, padx=0, side="right" )

		button1m = ttk.Button(self.l_frame, text='Criar Personagem', command= self.drawCreateCharScreen)
		button1m.pack(expand=True, padx=0)

		battle_button = ttk.Button(self.r_frame, text='Batalhar')
		battle_button.pack(expand=True, padx=0)
	#======================================= USUARIO
	#============Função de login 
	def login(self):
		username = self.login_frame.winfo_children()[2].get()
		password = self.login_frame.winfo_children()[4].get()
		user_input = User(username,password)
		user_usecase = user_factory()
		user = user_usecase.userLogin(user_input)

		if user is None:
			messagebox.showinfo("Login", "Login Falhou")
		else:
			messagebox.showinfo("Login", "Login realizado com sucesso !")
			self.logged_user = user

			self.drawMainScreen()
			self.login_frame.pack_forget()
			self.title('Menu')
			self.main_frame.pack(fill="both", expand=True)
		  

	#========= Função de registro 
	def register(self):
		username = self.login_frame.winfo_children()[2].get()
		password = self.login_frame.winfo_children()[4].get()

		user_input = User(username,password)
		user_usecase = user_factory()
		user = user_usecase.userRegister(user_input)

		if user is None:
			messagebox.showinfo("Registro", "Registro Falhou")
		else:
			messagebox.showinfo("Registro", "Registro realizado com sucesso !")
			self.logged_user = user
			self.drawMainScreen()
			self.login_frame.pack_forget()
			self.title('Menu')
			self.main_frame.pack(fill="both", expand=True)
			
	#=========Função de deletar
	def deleteUser(self):
		username = self.login_frame.winfo_children()[2].get()
		password = self.login_frame.winfo_children()[4].get()
		user_input = User(username,password)
		user_usecase = user_factory()
		user = user_usecase.deleteUser(user_input)
		messagebox.showinfo("Apagar", "Usuário foi apagado")


	#================ Função que esconde o menu principal e carrega a tela de criação de personagem ================
	def drawCreateCharScreen(self):
		self.main_frame.pack_forget()
		self.title('Criar Personagem')
		self.createchar_frame.pack(fill="both", expand=True)

	#=================== Função para cadastrar um novo personagem de um usuario ===================================
	def createChar(self):
		name = self.createchar_frame.winfo_children()[2].get()
		_class = self.createchar_frame.winfo_children()[4].get()
		char = self.controler.createUserCharacter(name, _class, self.logged_user)

		if char is None:
			messagebox.showinfo("Criação", "Criação de personagem falhou")
		else : 
			messagebox.showinfo("Criação", "Personagem criado com sucesso")
			self.createchar_frame.pack_forget()
			self.drawMainScreen()
			self.main_frame.pack(fill="both", expand=True)

	def deleteChar(self, char : Character):
		self.controler.deleteUserCharacter(char, self.logged_user)
		self.main_frame.pack_forget()
		self.drawMainScreen()
		self.main_frame.pack(fill="both", expand=True)


	# function to unload either the instructions or game frame, change the window title and load menu frame
	# since it is triggeret by both the button in game and instructions frame the button has to pass the frame to unload
	def back_to_main_menu(self, from_where):
		from_where.pack_forget()
		self.title('Main Menu')
		self.drawMainScreen()
		self.main_frame.pack(fill="both", expand=True)

