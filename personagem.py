
# Entidade responsavel por armazenar os personagens

class Personagem:
    
    def __init__(self,conta,apelido,classe):
        self.__conta = conta
        self.__apelido = apelido
        self.__classe = classe
    
    def __str__(self):
        conta = self.getConta()
        apelido = self.getApelido()
        classe = self.getClasse()
        return 'Conta = '+str(conta)+'\nApelido = '+str(apelido)+'\nClasse = '+str(classe)
    
    def getConta(self):
        return self.__conta
    
    def getApelido(self):
        return self.__apelido
    
    def getClasse(self):
        return self.__classe
    
    def setUsuario(self,nova_conta):
        self.__conta = nova_conta
        
    def setApelido(self,novo_apelido):
        self.__apelido = novo_apelido
        
    def setClasse(self,nova_classe):
        self.__classe = nova_classe
