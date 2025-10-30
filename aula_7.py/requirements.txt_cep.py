import requests

integrantes = {

"David": "123456789",
"Isla": "213456789",
"Marcelo": "321456789"

}

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br.ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f"{nome} mora em {cidade}")

else:
    print(f"Não foi possivel obter os dados para o cep {cep}")



