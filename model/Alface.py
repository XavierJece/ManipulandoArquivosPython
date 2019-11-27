class Alface:
    # Atributos
    tipo: None
    hco3:None
    so4:None
    cl:None
    ca:None
    mg:None
    na:None

    # Construtor
    def __init__(self, tipo, hco3, so4, cl, ca, mg, na):
        self.setTipo(tipo)
        self.setHCO3(hco3)
        self.setSO4(so4)
        self.setCL(cl)
        self.setCA(ca)
        self.setMG(mg)
        self.setNA(na)

    # Funções

    # Gets and Sets
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        if('l' in tipo.lower()):
            self.tipo = 'lisas'
        elif('c' in tipo.lower()):
            self.tipo = 'crespas'
        elif('r' in tipo.lower()):
            self.tipo = 'roxas'
        else:
            self.tipo = 'outro' 

    def getHCO3(self):
        return self.hco3
    def setHCO3(self, valor):
        self.hco3 = float(valor)

    def getSO4(self):
        return self.so4
    def setSO4(self, valor):
        self.so4 = float(valor)

    def getCL(self):
        return self.cl
    def setCL(self, valor):
        self.cl = float(valor)

    def getCA(self):
        return self.ca
    def setCA(self, valor):
        self.ca = float(valor)

    def getMG(self):
        return self.mg
    def setMG(self, valor):
        self.mg = float(valor)

    def getNA(self):
        return self.na
    def setNA(self, valor):
        self.na = float(valor)

    