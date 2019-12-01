#imports
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class GeraGrafico:
    # Atributos
    labelX = 'Fatores Químicos'
    labelY: None
    title = ' DOS FATORES QUÍMICOS NAS ALFACES '
    fig, ax = plt.subplots()
    
    # Construtor
    def __init__(self, eixoX, dados, tipoDeDado, variedade):
        self.labelY = tipoDeDado
        self.title = tipoDeDado + self.title + variedade.upper()
        
        if variedade == 'COMPARADAS':
            self.plotGraficoComparado(dados, eixoX)
        else:
            self.plotGrafico(variedade, dados, eixoX)

        self.fig.tight_layout()
        plt.show()

    # Funções
    def autolabel(self, rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            self.ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height/2),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', rotation=90)

    def definirCor(self, variedade):
        if variedade.lower() == 'lisas':
            return "#f390ea"
        elif variedade.lower() == 'crespas':
            return "#295d0f"
        elif variedade.lower() == 'roxas':
            return "#9400d3"
        else:
            return "#a0e403"
    
    def plotGrafico(self, variedade, dados, eixoX):
        x = np.arange(len(eixoX))   # the label locations
        width = .3                    # the width of the bars

        cor  = self.definirCor(variedade)

        # Plotando a barra Variedade Roxas
        self.relagle = self.ax.bar(x - width/20, 
            dados, 
            width, 
            label=variedade.upper(), 
            color=cor)
        self.autolabel(self.relagle)
        
        self.ax.set_ylabel(self.labelY)
        self.ax.set_xlabel(self.labelX)
        self.ax.set_title(self.title)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(eixoX)
        self.ax.legend()
    
    def plotGraficoComparado(self, dados, eixoX):
        x = np.arange(len(eixoX))   # the label locations
        width = .3                    # the width of the bars


        i = 0
        for dado in dados:
            if i == 0:
                cor = self.definirCor('lisas')
                lbl = 'LISAS'
                pos = x - width*2
            elif i == 1:
                cor = self.definirCor('crespas')
                lbl = 'CRESPAS'
                pos = x - width
            else:
                cor = self.definirCor('roxas')
                lbl = 'ROXAS'
                pos = x - width/20
            # Plotando a barra Variedade Lisas
            relagle= self.ax.bar(pos, 
                dado, 
                width, 
                label=lbl, 
                color=cor)
            self.autolabel(relagle)
            i += 1
        
        self.ax.set_ylabel(self.labelY)
        self.ax.set_xlabel(self.labelX)
        self.ax.set_title(self.title)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(eixoX)
        self.ax.legend()
        

    # Gets and Sets
