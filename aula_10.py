import csv 
import random 
with open("dados.csv", mode="w", newline="", encoding="utf-8") as arquivo:
    escritor_csv = csv.writer(arquivo)
#
    escritor_csv.writerow(["nome", "idade", "cidade"])
#

    escritor_csv.writerow(["Ana", 28, "Recife"])
    escritor_csv.writerow(["João", 45, "Recife"])
    escritor_csv.writerow(["Mariana", 31, "Recife"])

    escritor_csv.writerow(["Bruno", 34, "São Paulo"])
    escritor_csv.writerow(["Lucas", 29, "São Paulo"])

    escritor_csv.writerow(["Carla", 25, "Salvador"])
    




    print("arquivos dados csv criado com sucesso!")
    
    #Filtre os dados para aparecer apenas moradores de recife
    

with open("dados.csv", mode="r", encoding="utf-8") as arquivo:
    leitor_csv = csv.reader(arquivo)
    cabecalho = next(leitor_csv)  # pula a primeira linha (título das colunas)
    
    print("\nMoradores de Recife:")
    for linha in leitor_csv:
        nome, idade, cidade = linha
        if cidade == "Recife":
            print(f"{nome}, {idade} anos, {cidade}")