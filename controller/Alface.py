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
        
        # print(dados)

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

    def listaAlfaceEspecifica(self, arquivo, variedade, atributo):
        listaGeral = self.listaAlface(arquivo)

        listEspecifica = []

        if variedade != "":
            for alface in listaGeral:
                if(variedade.lower() in alface.getTipo().lower()):
                    if str(atributo).lower() == "variedade":
                        listEspecifica.append(alface.getTipo())
                    elif str(atributo).lower() == "hco3":
                        listEspecifica.append(alface.getHCO3())
                    elif str(atributo).lower() == "so4":
                        listEspecifica.append(alface.getSO4())
                    elif str(atributo).lower() == "cl":
                        listEspecifica.append(alface.getCL())
                    elif str(atributo).lower() == "ca":
                        listEspecifica.append(alface.getCA())
                    elif str(atributo).lower() == "mg":
                        listEspecifica.append(alface.getMG())
                    elif str(atributo).lower() == "na":
                        listEspecifica.append(alface.getNA())
                    elif str(atributo).lower() == "":
                        listEspecifica.append(alface)
                    
                    
        else:
            for alface in listaGeral:
                if str(atributo).lower() == "variedade":
                    listEspecifica.append(alface.getTipo())
                elif str(atributo).lower() == "hco3":
                    listEspecifica.append(alface.getHCO3())
                elif str(atributo).lower() == "so4":
                    listEspecifica.append(alface.getSO4())
                elif str(atributo).lower() == "cl":
                    listEspecifica.append(alface.getCL())
                elif str(atributo).lower() == "ca":
                    listEspecifica.append(alface.getCA())
                elif str(atributo).lower() == "mg":
                    listEspecifica.append(alface.getMG())
                elif str(atributo).lower() == "na":
                    listEspecifica.append(alface.getNA())
                elif str(atributo).lower() == "":
                    listEspecifica.append(alface)

        return listEspecifica



    
    # Gets and Sets
