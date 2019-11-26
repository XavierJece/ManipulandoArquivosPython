# Imports
from controller.Alface import *
from statistics import *
from view.TelaApresenta import *



# mediaGeral = []
# mediaLisas = []
# mediaCrespas = []
# mediaRoxas = []

# for variedade in variedadesAlface:
#     for fator in fatoresQuimicos:

#         try:
#             valor = median(controlAlface.listaAlfaceEspecifica(nomeArquivo, variedade, fator))
#             valor = round(valor,2)
#             print(valor)
#         except:
#             print('Não tem nenhum valor que se repete')
        
#         if variedade.lower() == '':
#             mediaGeral.append(valor)
#         elif variedade.lower() == 'lisa':
#             mediaLisas.append(valor)
#         elif variedade.lower() == 'crespa':
#             mediaCrespas.append(valor)
#         elif variedade.lower() == 'roxa':
#            mediaRoxas.append(valor)

# GeraGrafico(fatoresQuimicos, mediaGeral, mediaLisas, mediaCrespas, mediaRoxas, 'Desvio Padrão', 'geral')

ta=TelaApresenta()