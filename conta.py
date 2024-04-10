# Entidade responsável por armazenar as contas

class Conta:
    
    def __init__(self,usuario,senha,lista_personagens):
        self.__usuario = usuario
        self.__senha = senha
        self.__lista_personagens = lista_personagens        
        
    def __str__(self):
        personagens = list()
        lista_personagens = self.getPersonagens()
        usuario = self.getUsuario()
        senha = self.getSenha()
        for i in range(0,len(lista_personagens)):
            apelido = lista_personagens[i].getApelido()
            personagens.append(apelido)
        return 'Usuário = '+str(usuario)+'\nSenha = '+str(senha)+'\nPersonagens ='+str(personagens)+'\n__________________'
    
    def getUsuario(self):
        return self.__usuario

    def getSenha(self):
        return self.__senha
    
    def getPersonagens(self):
        return self.__lista_personagens
    
    def setUsuario(self,novo_usuario):
        self.__usuario = novo_usuario
        
    def setSenha(self,nova_senha):
        self.__senha = nova_senha
        
    def setPersonagens(self,nova_lista_personagens):
        self.__lista_personagens = nova_lista_personagens 