# Imports
from model.Leitor import *

leitor = Leitor("acp_alface")

dados = leitor.ler()
contador = 0

for dado in dados:
    print(dado)