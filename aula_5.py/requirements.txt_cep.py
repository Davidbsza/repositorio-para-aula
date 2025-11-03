import requests

integrantes = {

"David": "11630097",
"Isla": "11630097",
"Marcelo": "11630099"

}

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        
        dados = resposta.json()
        cidade = dados.get("localidade", "Cidade não encontrada")
        print(f"{nome} mora em {cidade}")

    else:
        print(f"Não foi possivel obter os dados para o cep {cep}")



