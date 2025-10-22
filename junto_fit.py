# --- SISTEMA DE FREQUÊNCIA DA JUNTOFIT ---

# Variáveis iniciais
frequencia_seguida = 0
frequencia_total = 0

while True:
    print("\n=== CATRACA JUNTOFIT ===")
    entrada = input("O aluno compareceu hoje? (s/n ou 'sair' para encerrar): ").strip().lower()

    if entrada == "sair":
        print("\nEncerrando sistema. Até logo!")
        break

    if entrada == "s":
        frequencia_total += 1
        frequencia_seguida += 1

        if frequencia_seguida < 21:
            print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO!")
            print(f"Faltam {21 - frequencia_seguida} dias para completar a promoção.")
        elif frequencia_seguida == 21:
            print("🎉 UHUU! AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ! 🎁")
        else:
            # Após completar 21, ele continua, mas o contador pode ser reiniciado se quiser
            print("Você já completou a promoção! Continue treinando firme 💪")

    elif entrada == "n":
        print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO.")
        frequencia_seguida = 0  # Zera a contagem

    else:
        print("Entrada inválida. Digite apenas 's', 'n' ou 'sair'.")
