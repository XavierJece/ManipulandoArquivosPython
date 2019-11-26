#imports
import tkinter as tk
from controller.Alface import *
from statistics import *
# from view.GeraGrafico import GeraGrafico

class TelaApresenta:
    # Atributos
    janeta: None
    nomeArquivo = 'acp_alface'
    # Contrutor
    def __init__(self):
        self.janela = tk.Tk()
        self.janela.title("Tela Principal")
        self.janela.geometry("500x500+100+100") #LxA+E+T

        #adicionando dados gerais
        self.dadosGeral()
        
        # Plotando janela
        self.janela.mainloop()

    # Funções
    def dadosGeral(self):
        # Definindo Titulo
        lbTituloGeral = tk.Label(self.janela, text="Estátisticas Geral")
        lbTituloGeral["font"] = ("Arial", "10", "bold")
        lbTituloGeral.place(x=10, y=10)

        # Valores para apresentação
        media = self.valores("", 'media')
        moda = self.valores("", 'moda')
        mediana = self.valores("", 'mediana')
        dp = self.valores("", 'dp')

        #Botoes'Cl', 'Ca', 'Mg', 'Na'
        textLabel = "Média dos Fatores Químicos"
        textLabel = textLabel, "\nHCO3 = ", media[0]
        textLabel = textLabel, "\nSO4 = ", media[1]
        textLabel = textLabel, "\nCl = ", media[2]
        textLabel = textLabel, "\nCa = ", media[3]
        textLabel = textLabel, "\nMg = ", media[4]
        textLabel = textLabel, "\nNa = ", media[5]

        lblMedia = tk.Label(self.janela, text=textLabel)
        lbTituloGeral["font"] = ("Arial", "10")
        lbTituloGeral.place(x=10, y=30)
        
        
        # btnMedia = tk.Button(self.janela, width=20, text="Gerar Gráfico",command=self.graficoGeralMedia )
        # btnMedia.place(x=10, y=30)



        # btnMediana = tk.Button(self.janela, width=20, text="Gerar Gráfico",command=self.graficoGeralMediana )
        # btnMediana.place(x=10, y=55)

        # btnDp = tk.Button(self.janela, width=20, text="Gerar Gráfico",command=self.graficoGeralDp )
        # btnDp.place(x=10, y=80)

    def fecharJanela(self):
        self.anela.destroy()

    def graficoGeral(self):
        print('teste')

    def valores(self, variedade, conta):
        fatoresQuimicos = ['HCO3', 'SO4', 'Cl', 'Ca', 'Mg', 'Na']

        resultadosFatores = []

        for fator in fatoresQuimicos:

            if conta == 'moda':
                try:
                    valor = mode(controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                    valor = round(valor,2)
                    print(valor)
                except:
                    valor = 'Moda não encontrada:('
            
            elif conta == 'media':
                try:
                    valor = mean(controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                    valor = round(valor,2)
                    print(valor)
                except:
                    valor = 'Média não encontrada :('
            elif conta == 'mediana':
                try:
                    valor = median(controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                    valor = round(valor,2)
                    print(valor)
                except:
                    valor = 'Mediana não encontrada :('
            elif conta == 'dp':
                try:
                    valor = pstdev(controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                    valor = round(valor,2)
                    print(valor)
                except:
                    valor = 'Mediana não encontrada :('
            
            resultadosFatores.append(valor)

        return resultadosFatores
            



    # Gets and Sets

