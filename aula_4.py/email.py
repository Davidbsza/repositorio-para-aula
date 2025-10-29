
# Validar dominio do email.



def verificar_dominio(email_usuario):
    """Verifica se o domínio '@jogajuntoinstituto.org' está contido no e-mail."""
    
    # 1. Define o domínio alvo para comparação
    DOMINIO_ALVO = "@jogajuntoinstituto.org"
    
    # 2. Usa o operador 'in' do Python para verificar a presença da substring
    if DOMINIO_ALVO in email_usuario:
        return True
    else:
        return False

# 3. Input do Usuário
# Pede o e-mail e usa .strip() para remover espaços extras no início/fim
email_digitado = input("Digite seu e-mail para verificação: ").strip()

# 4. Execução e Output
if verificar_dominio(email_digitado):
    print(f"\n SUCESSO! O e-mail '{email_digitado}' é VÁLIDO para o instituto.")
else:
    print(f"\n FALHA! O e-mail '{email_digitado}' NÃO contém o domínio correto.")

Funcionalidade: testar validação do Instituto

  Cenário: [SUCESSO] O sistema deve aceitar um e-mail com o domínio correto.

    Dado que o usuário está na tela de cadastro/login
    E que o domínio correto do instituto é "@jogajuntoinstituto.org"

    Quando o usuário digita o e-mail "joao.silva@jogajuntoinstituto.org"
    E a função de validação é executada

    Então o sistema deve retornar 'VERDADEIRO' (True)
    E o usuário deve receber a mensagem de sucesso: "O e-mail é VÁLIDO para o instituto."