import pandas as pd

# Criar os dados em formato de dicionario

dados = { 
    "nome": ["Ana", "Bruno", "Carlos", "Diona"],
    "idade": [23, 35, 45, 29],
    "Cidade": ["São Paulo", "rio de janeiro", "belo horizonte", "salvador"]
}
# Criar o dataframe

df = pd.DataFrame(dados)

# exibir o dataframe completo

print("dataframe completo:\n, df)")
print(df)

# Filtrar apenas os moradores de Salvador
Salvador_df = df[df["Cidade"] == "salvador"]
print("\n Moradores de Salvador:\n")
print(Salvador_df)