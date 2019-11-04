# acp_alface = open("acp_alface.txt", r)

ref_arquivo = open("acp_alface.txt","r")

Valores_HCO3 = []
Valores_SO4 = []
Valores_CL = []
Valores_CA = []
Valores_MG = []
Valores_NA = []

for linha in ref_arquivo:
    # valores = linha.split()

    Valores_HCO3.append(linha.split()[1])
    Valores_SO4.append(linha.split()[2])
    Valores_CL.append(linha.split()[3])
    Valores_CA.append(linha.split()[4])
    Valores_MG.append(linha.split()[5])
    Valores_NA.append(linha.split()[6])

ref_arquivo.close()

i = 1
valorTotal = 0.0
while i < len(Valores_SO4):
    print("Valor: " + Valores_SO4[i])
    valorTotal = valorTotal +  float(Valores_SO4[i])
    i+=1
print("Valor Total: ", valorTotal)