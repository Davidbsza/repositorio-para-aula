import csv 

with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor_csv = csv.writer(arquivo)
#
    escritor_csv.writerow(["nome", "idade", "cidade"])
#

    escritor_csv.writerow(["Ana", 28, "São Paulo"])
    escritor_csv.writerow(["Bruno", 34, "Rio de Janeiro"])
    escritor_csv.writerow(["Carla", 25, "Belo horizonte"])

    print("arquivos dados csv criado com sucesso!")
    
    