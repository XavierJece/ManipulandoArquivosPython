# Imports
from controller.Alface import *
from statistics import *
import os
# import time
from view.GeraGrafico import *

class Principal:

    # Atributos
    fatoresQuimicos = ['HCO3', 'SO4', 'Cl', 'Ca', 'Mg', 'Na']
    variedadesEstatistica = ['media', 'moda', 'mediana', 'dp']
    nomeArquivo = 'acp_alface'
    controlAlface = Controller()

    # Contrutor
    def __init__(self):
        self.apresentacaoMenu()
        
    # Funções
    def apresentacaoMenu(self):
        print(" |------------------------------|")
        print(" | APRESENTAÇÃO DA ESTATÍSTICAS |")
        print(" |      DOS FATORES QUÍMICOS    |")
        print(" |    DAS VARIEDADES DE ALFACE  |")
        print(" |------------------------------|")
        print(" |------------------------------|")
        print(" |    Escolha uma Variedade!    |")
        print(" |------------------------------|")
        print(" | 1 |          GERAL           |")
        print(" |------------------------------|")
        print(" | 2 |          LISAS           |")
        print(" |------------------------------|")
        print(" | 3 |         CRESPAS          |")
        print(" |------------------------------|")
        print(" | 4 |          ROXAS           |")
        print(" |------------------------------|")
        print(" | 5 | GRÁFICO DE COMPARAÇÃO    |")
        print(" |------------------------------|")
        print(" | 0 |          SAIR            |")
        print(" |------------------------------|")
        entrada = input(" => ")
        
        # Limpar a tela
        os.system("cls")

        self.analiseDaEntradaMenu(entrada)

    def apresentacaoDespedida(self):
        print(" TCHAU")

    def apresentacaoEntradaInvalida(self):
        print(" Entrada Inválida")

    def apresentacaoValores(self, variedade):
        
        print(" |------------------------------|")
        print(" | APRESENTAÇÃO DA ESTATÍSTICAS |")
        print(" |      DOS FATORES QUÍMICOS    |")
        print(" |    DAS VARIEDADES DE ALFACE  |")
        print(" |------------------------------|")

        if variedade == "":
            print(" |            GERAL             |")
        else:
            print(" |     ALFACES ", variedade.upper())
        
        print(" |------------------------------|")
        for estatistica in self.variedadesEstatistica:
            
            print(" |            ", estatistica.upper())
            for fator in self.fatoresQuimicos:

                print(" |  => ", fator.upper(), "=> ", self.valor(variedade, fator, estatistica))
            
            print(" |------------------------------|")

        self.apresentacaoMenuGrafico(variedade)

    def apresentacaoMenuGrafico(self, variedade):
        print(" | 1 |     Gráfio Média         |")
        print(" |------------------------------|")
        print(" | 2 |    Gráfio Mediana        |")
        print(" |------------------------------|")
        print(" | 3 |       Gráfio DP          |")
        print(" |------------------------------|")
        print(" | 4 |          MENU            |")
        print(" |------------------------------|")
        print(" | 0 |          SAIR            |")
        print(" |------------------------------|")
        entrada = input(" => ")

        self.analiseDaEntradaMenuGrafico(entrada, variedade)

    def apresentacaoMenuComparacao(self):
        print(" |------------------------------|")
        print(" | 1 |     Gráfio Média         |")
        print(" |------------------------------|")
        print(" | 2 |    Gráfio Mediana        |")
        print(" |------------------------------|")
        print(" | 3 |       Gráfio DP          |")
        print(" |------------------------------|")
        print(" | 4 |          MENU            |")
        print(" |------------------------------|")
        print(" | 0 |          SAIR            |")
        print(" |------------------------------|")
        entrada = input(" => ")

        self.analiseDaEntradaMenuGrafico(entrada, "COMPARADAS")

    def analiseDaEntradaMenu(self,entrada):

        if entrada == '1':
            self.apresentacaoValores('')
        elif entrada == '2':
            self.apresentacaoValores('lisas')
        elif entrada == '3':
            self.apresentacaoValores('crespas')
        elif entrada == '4':
            self.apresentacaoValores('roxas')
        elif entrada == '5':
            self.apresentacaoMenuComparacao()
        elif entrada == '0':
            self.apresentacaoDespedida()
        else:
            self.apresentacaoEntradaInvalida()

    def analiseDaEntradaMenuGrafico(self,entrada, variedade):

        if entrada == '1':
            if variedade == 'COMPARADAS':
                self.apresentacaoGraficoComparado('media')
            else:
                self.apresentacaoGrafico(variedade, 'media')
        elif entrada == '2':
            if variedade == 'COMPARADAS':
                self.apresentacaoGraficoComparado('mediana')
            else:
                self.apresentacaoGrafico(variedade, 'mediana')
        elif entrada == '3':
            if variedade == 'COMPARADAS':
                self.apresentacaoGraficoComparado('dp')
            else:
                self.apresentacaoGrafico(variedade, 'dp')
        elif entrada == '4':
            # Limpa Tela
            os.system("cls")
            self.apresentacaoMenu()
        elif entrada == '0':
            # Limpa Tela
            os.system("cls")
            self.apresentacaoDespedida()
        else:
            # Limpa Tela
            os.system("cls")
            self.apresentacaoEntradaInvalida()

    def valor(self, variedade, fator, estatistica):
        
        if estatistica == "media":
            valor = mean(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
            return round(valor,2)
        elif estatistica == "moda":
            try:
                valor = mode(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                return round(valor,2)
            except:
                return "Moda não encontrada"
        elif estatistica == "mediana":
            valor = median(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
            return round(valor,2)
        elif estatistica == "dp":
            valor = pstdev(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
            return round(valor,2)
            
    def apresentacaoGrafico(self, variedade, estatistica):
        if variedade == "":
            v = "TODAS"
        else:
            v = variedade

        medidas = []

        for fator in self.fatoresQuimicos:
        
            if estatistica == "media":
                valor = mean(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                medidas.append(round(valor,2))
            elif estatistica == "mediana":
                valor = median(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                medidas.append(round(valor,2))
            elif estatistica == "dp":
                valor = pstdev(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, variedade, fator))
                medidas.append(round(valor,2))
        
        GeraGrafico(self.fatoresQuimicos, medidas, estatistica.upper(), v.upper())

    def apresentacaoGraficoComparado(self, estatistica):
        variedadeAlface = ['lisas', 'crespas', 'roxas']
        medidasCompletas = []
        medidas1 = []
        medidas2 = []
        medidas3 = []
        
        i = 0
        for alface in variedadeAlface:
            for fator in self.fatoresQuimicos:
        
                if estatistica == "media":
                    valor = mean(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, alface, fator))
                elif estatistica == "mediana":
                    valor = median(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, alface, fator))
                elif estatistica == "dp":
                    valor = pstdev(self.controlAlface.listaAlfaceEspecifica(self.nomeArquivo, alface, fator))
                if i == 0:
                    medidas1.append(round(valor,2))
                elif i == 1:
                    medidas2.append(round(valor,2))
                else:
                    medidas3.append(round(valor,2))
            i += 1

        medidasCompletas.append(medidas1)
        medidasCompletas.append(medidas2)
        medidasCompletas.append(medidas3)

        GeraGrafico(self.fatoresQuimicos, medidasCompletas, estatistica.upper(), 'COMPARADAS')

Principal()