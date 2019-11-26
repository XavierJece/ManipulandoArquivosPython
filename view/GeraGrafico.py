#imports
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class GeraGrafico:
    # Atributos
    labelX = 'Fatores Químicos'
    labelY: None
    title = ' dos Fatores Químicos nas Variedades de Alfaces'
    relagleGeral: None
    relagleLisas: None
    relagleCrespas: None
    relagleRoxas: None
    fig, ax = plt.subplots()
    
    # Construtor
    def __init__(self, eixoX, geral, lisas, crespas, roxas, tipoDeDado, barrasApresentar):
        self.labelY = tipoDeDado
        self.title = tipoDeDado + self.title

        x = np.arange(len(eixoX))   # the label locations
        width = .3                    # the width of the bars

        if barrasApresentar == 'geral':
            # Plotando a barra Variedade Geral
            self.relagleGeral = self.ax.bar(x - width*3, 
                geral, 
                width, 
                label='Geral', 
                color='#a0e403')
            self.autolabel(self.relagleGeral)
        elif barrasApresentar == 'lisa':
            # Plotando a barra Variedade Lisas
            self.relagleLisas = self.ax.bar(x - width*2, 
                lisas, 
                width, 
                label='Lisas', 
                color='#f390ea')
            self.autolabel(self.relagleLisas)  
        elif barrasApresentar == 'crespa':
            # Plotando a barra Variedade Crespas
            self.relagleCrespas = self.ax.bar(x - width, 
                crespas, 
                width, 
                label='Crespas', 
                color='#295d0f')      
            self.autolabel(self.relagleCrespas)
        elif barrasApresentar == 'roxa':
            # Plotando a barra Variedade Roxas
            self.relagleRoxas = self.ax.bar(x - width/20, 
                roxas, 
                width, 
                label='Roxas', 
                color='#9400d3')
            self.autolabel(self.relagleRoxas)
        elif barrasApresentar == 'comparar':
            # Plotando a barra Variedade Lisas
            self.relagleLisas = self.ax.bar(x - width*2, 
                lisas, 
                width, 
                label='Lisas', 
                color='#f390ea')
            self.autolabel(self.relagleLisas)  
            # Plotando a barra Variedade Crespas
            self.relagleCrespas = self.ax.bar(x - width, 
                crespas, 
                width, 
                label='Crespas', 
                color='#295d0f')      
            self.autolabel(self.relagleCrespas)
            # Plotando a barra Variedade Roxas
            self.relagleRoxas = self.ax.bar(x - width/20, 
                roxas, 
                width, 
                label='Roxas', 
                color='#9400d3')
            self.autolabel(self.relagleRoxas)

        self.ax.set_ylabel(self.labelY)
        self.ax.set_xlabel(self.labelX)
        self.ax.set_title(self.title)
        self.ax.set_xticks(x)
        self.ax.set_xticklabels(eixoX)
        self.ax.legend()
        
        

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

    # Gets and Sets
