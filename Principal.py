# Imports
from controller.Alface import *
from model.Alface import *
from statistics import *
from view.GeraGrafico import *

controlAlface = Controller()
nomeArquivo = 'acp_alface'

fatoresQuimicos = ['HCO3', 'SO4', 'Cl', 'Ca', 'Mg', 'Na']
variedadesAlface = ['', 'lisa', 'crespa', 'roxa'] # o vazio representa o Geral

mediaGeral = []
mediaLisas = []
mediaCrespas = []
mediaRoxas = []

for variedade in variedadesAlface:
    for fator in fatoresQuimicos:

        try:
            valor = median(controlAlface.listaAlfaceEspecifica(nomeArquivo, variedade, fator))
            valor = round(valor,2)
            print(valor)
        except:
            print('Não tem nenhum valor que se repete')
        
        if variedade.lower() == '':
            mediaGeral.append(valor)
        elif variedade.lower() == 'lisa':
            mediaLisas.append(valor)
        elif variedade.lower() == 'crespa':
            mediaCrespas.append(valor)
        elif variedade.lower() == 'roxa':
           mediaRoxas.append(valor)

GeraGrafico(fatoresQuimicos, mediaGeral, mediaLisas, mediaCrespas, mediaRoxas, 'Desvio Padrão', 'geral')

