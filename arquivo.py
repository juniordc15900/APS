from conta import Conta
from personagem import Personagem
import os
import re
# Classe responsavel para executar ações do tipo leitura/escrita de arquivos
class Arquivo:

    # Lê todos os personagens de uma certa conta (auxilia a função leituraContas())
    def leituraPersonagens(self,nome_personagens):
        # Cria uma lista de personagem
        lista_personagens = list()
        # Percorre todos os personagens na lista recebida (nome_personagens)
        for i in range(0,len(nome_personagens)): 
            # Abre o arquivo do player na posição "i" do vetor de players
            arquivo = open('personagens/'+str(nome_personagens[i])+'.txt', 'r') 
            arquivo_personagem = arquivo.read()
            # Divide o conteudo lido em uma lista que separa cada elemento quando encontra ";" no arquivo
            atributos_personagem = arquivo_personagem.split(';')
            arquivo.close()
            # Cria um objeto personagem e grava ele na lista de personagens
            personagem = Personagem(atributos_personagem[0], atributos_personagem[1], atributos_personagem[2])
            lista_personagens.append(personagem)

        return lista_personagens # retorna a lista de personagens para a conta correspondente

    
    # Lê todas as contas já gravadas ao inicializar o programa
    def leituraContas(self):
        # Lista todos os arquivos que estão na pasta selecionada
        nome_contas = os.listdir('contas/')
        contas = list()
        # Percorre todos elementos da lista criada
        for i in range(0,len(nome_contas)):
            # Evita erros na plataforma jupyter ou alguma outra que utilize "ipynb" (arquivo de checkpoint)
            if(nome_contas[i] != '.ipynb_checkpoints'):
                # Abre e lê todos arquivos da pasta de contas
                arquivo = open('contas/'+str(nome_contas[i]), 'r')
                arquivo_conta = arquivo.read()
                # Separa os elementos dentro do arquivo por ";" e logo após separa os personagens por ","
                atributos_conta = arquivo_conta.split(';')
                nome_personagens = atributos_conta[2].split(',')
                # Caso exista algum personagem na conta, ative o leituraPersonagem() se não simplesmente personagens é uma lista vazia
                if(atributos_conta[2] != ''):
                    personagens = Arquivo().leituraPersonagens(nome_personagens)
                else:
                    personagens = list()
                arquivo.close()
                # Cria um objeto do tipo Conta e armazena ele na lista de contas
                conta = Conta(atributos_conta[0],atributos_conta[1],personagens)
                contas.append(conta)
        return contas # Retorna a lista de contas para o jogo
     
    # Salva o arquivo de uma conta especifica na pasta de contas
    def salvarConta(self,conta):
        # Cria o arquivo com o nome de usuario da conta e grava o texto com usuario e senha separado por ";"
        arquivo = open('contas/'+conta.getUsuario()+'.txt', 'w')
        texto = str(conta.getUsuario())+';'+str(conta.getSenha())+';'
        arquivo.writelines(texto)
        arquivo.close()
        
    # Deleta o arquivo de uma conta especifica na pasta de contas
    def deletarConta(self,conta):
        # Se existirem personagens na conta, percorra todos arquivos de personagens deletando um por um
        lista_personagens = conta.getPersonagens()
        for i in range(0,len(lista_personagens)):
                personagem = lista_personagens[i].getApelido()
                os.remove('personagens/'+personagem+'.txt')
        # Deleta o arquivo da conta
        os.remove('contas/'+conta.getUsuario()+'.txt')
    
    # Salva o arquivo do personagem especifico na pasta personagens e modifica o arquivo de conta em que ele pertence
    def salvarPersonagem(self, personagem, conta):
        # Abre o arquivo da conta e adiciona o personagem nele
        nome_conta = personagem.getConta()
        apelido = personagem.getApelido()
        classe = personagem.getClasse()
        arquivo = open('contas/'+nome_conta+'.txt', 'a')
        lista_personagens = conta.getPersonagens()
        if(len(lista_personagens) > 1):
            arquivo.write(','+str(apelido))
        else:
            arquivo.write(str(apelido))
        arquivo.close()
        # Cria o arquivo personagem na pasta personagens
        arquivo = open('personagens/'+apelido+'.txt', 'w')
        arquivo.write(str(nome_conta)+';'+str(apelido)+';'+str(classe))
        arquivo.close()
    
    # Deleta o arquivo de um personagem especifico e remove ele no arquivo de sua conta correspondente
    def deletarPersonagem(self,personagem):
        apelido = personagem.getApelido()
        conta = personagem.getConta()
        # Deleta o arquivo na pasta personagens
        os.remove('personagens/'+apelido+'.txt')
        # Lê o arquivo de conta onde o personagem se encontra
        arquivo = open('contas/'+conta+'.txt','r')
        arquivo_conta = arquivo.read()
        arquivo.close()
        # Faz a separação dos elementos do arquivo conta inclusive dos personagens
        atributos_conta = arquivo_conta.split(';')
        nome_personagens = atributos_conta[2].split(',')
        # Procura o personagem especifico na lista de personagens da conta
        if(apelido in nome_personagens):
            # Remove o personagem da lista
            nome_personagens.remove(apelido)
        # Se restou uma lista, separe os elementos por "," e una eles em uma string
        if(type(nome_personagens) == list):
            nome_personagens = ','.join(map(str, nome_personagens))
        else:
            nome_personagens = ''
        atributos_conta[2] = nome_personagens
        # una todos atributos da conta anteriormente separados com ";" como separador
        texto = ';'.join(map(str, atributos_conta))
        # Abre o arquivo da conta especifica e salve as alterações
        arquivo = open('contas/'+conta+'.txt','w')
        arquivo.write(texto)
        arquivo.close()