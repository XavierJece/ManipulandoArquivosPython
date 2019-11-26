# Imports
from controller.Alface import *
from model.Alface import *
from statistics import *

controlAlface = Controller()

nomeArquivo = 'acp_alface'

# dados = controlAlface.listaAlface(nomeArquivo)
dados = controlAlface.listaAlfaceEspecifica(nomeArquivo, 'l', 'hco3')

for dado in dados:
    print(dado)


print ("Media: ", mean(dados))