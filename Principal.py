# Imports
from controller.Alface import *
from model.Alface import *

controlAlface = Controller()

nomeArquivo = 'acp_alface'

# dados = controlAlface.listaAlface(nomeArquivo)
dados = controlAlface.listaAlfaceEspecifica(nomeArquivo, 'l')

for dado in dados:
    print(dado.getTipo())