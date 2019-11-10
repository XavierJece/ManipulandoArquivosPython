# imports
import os 


class Leitor():
    # Atributos
    arquivo:None
    
    # Contrutor
    def __init__(self, arquivo):
        self.arquivo = arquivo
    
    # Funções
    def ler(self):
        # Caminho absoluto
        # dir_path = os.path.dirname(os.path.realpath(__file__))
        # Caminho Relativo
        path = os.getcwd()
        caminho = path + "\\database\\" + str(self.arquivo) + ".txt"
        
        # Abrir o arquivo em modo de leitura 
        ref_arquivo = open(caminho,"r")
        
        #vetor para retornar os dados lidos
        valores = []
        
        # lendo linha por linha
        for linha in ref_arquivo:
            # Add dados da linha no vetor
            valores.append(linha.split())
        
        # Fechando o arquivo
        ref_arquivo.close()
        
        # deletando a linha que está o titulo das colunas
        del valores[0]

        # retordando dados
        return valores

    # Gets and Sets