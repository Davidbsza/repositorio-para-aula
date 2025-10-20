# Programa: soma de duas notas
nome = input("digite seu nome: ")
# Captura das notas
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
nota4 = float(input("digite a quarta nota "))


# Soma das notas

soma = (nota1 + nota2 + nota3 + nota4 ) /4


# Exibição do resultado

print("\n--- Resultado ---")
print(f"Soma das notas: {nome} sua media é {soma:.2f}")
