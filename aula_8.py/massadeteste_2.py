from faker import Faker
import csv

fake = Faker ("pt_br")

nome = fake.name()
nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
idade = (2025 - nascimento.year)
cidade = fake.city()
print(nome, cidade, idade)

def criar_persona_lista():
    persona_lista = []
    
    for i in range(10):
        nome = fake.name()
        persona_lista.append(nome)
    return (persona_lista)

print(criar_persona_lista())
