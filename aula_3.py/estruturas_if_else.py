# Solicita a idade do usuário
idade = int(input("Digite sua idade: "))

# Verifica se é maior ou igual a 18
if idade >= 18:
    print("Indivíduo possui idade mínima para dirigir")

# Solicita o nome e a idade do usuário
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

# Verifica se a idade é um número válido
if not idade.isdigit():
    print("Por favor, digite uma idade válida (apenas números).")
else:
    idade = int(idade)  # converte para inteiro

    # Estruturas condicionais
    if idade < 0:
        print("Idade inválida. Tente novamente.")
    elif idade < 18:
        print(f"{nome}, você ainda NÃO possui idade mínima para dirigir.")
        print("Aguarde até completar 18 anos.")
    elif idade == 18:
        print(f"{nome}, você acabou de atingir a idade mínima para dirigir! Parabéns!")
    else:
        print(f"{nome}, você possui idade mínima para dirigir.")
        print("Lembre-se de sempre dirigir com responsabilidade.")
