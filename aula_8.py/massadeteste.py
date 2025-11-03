from faker import Faker

fake = Faker("pt_br")
print("nome:", fake.name())
print("email:", fake. email())
print("cidade:", fake.city())
