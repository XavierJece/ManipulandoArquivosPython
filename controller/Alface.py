# imports
from model.Leitor import *
from model.Alface import *

class Controller:
    # Atributos
    # Contrutor
    # Funções
    
    def listaAlface(self, arquivo):
        leitor = Leitor(arquivo)
        dados = leitor.ler()
        
        listRetorno = []
        
        for dado in dados:
            alface = Alface(
                dado[0],
                dado[1],
                dado[2],
                dado[3],
                dado[4],
                dado[5],
                dado[6]                
            )
            listRetorno.append(alface)
        return listRetorno



    
    # Gets and Sets
