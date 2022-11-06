'''any e all
all -> retorna true se todos os elementos do iteravel sao vdd ou ainda se o iterável está vazio
Exemplos:'''

print(all([0, 1, 2, 3, 4])) #Todos os números são verdadeiros? False devido ao zero

print(all([1, 2, 3, 4])) #Todos os números são verdadeiros? True

print(all([])) #Todos os números são verdadeiros? True

print(all((1, 2, 3, 4))) #Todos os números são verdadeiros? True

print(all({1, 2, 3, 4})) #Todos os números são verdadeiros? True

print(all("Gueek")) #Todos os números são verdadeiros? True

nomes = ["Amanda", "Antonio", "Ana", "Andressa", "Alessandro"]

print(all([nome[0] == "A" for nome in nomes]))

'''any() -> Retorna True se qualquer elemento for verdadeiro e False se for vazio'''
print(any([0, 1, 2, 3, 4])) #True

print(any([0, False, [], (), {}])) #False

nomes = ['Marcos', 'Maria', 'Marcio', 'Messias', 'Vanessa']

print(any([nome[0] == "M" for nome in nomes]))

print(any(num for num in [4, 2, 10, 6, 8, 9] if num % 2 ==0))
