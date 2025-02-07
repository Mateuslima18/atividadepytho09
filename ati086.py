# Dicionário de pessoas com idades  
people = {  
    "Rafael": 10,  
    "GASPAZIN": 15,  
    "Jen": 30,  
    "ROMULO DO GRAU": 20,  
    "Mateus O ANÃO": 19,  
    "PAULO DO CALOTE": 17,  
    "ITALO PISICO": 34,  
    "MAMEDE DA IRMÃZINHA": 20,  
    "NICOLAS": 24,  
    "ELYTON LGBTQQICAAPF2K+": 60,  
}  

 
nomes_ordenados = sorted(people.keys())  

  
print("Nomes em ordem alfabética:")  
for nome in nomes_ordenados:  
    print(nome)  

  
soma_idades = sum(people.values())  

 
media_idades = soma_idades / len(people)  

 
pessoa_mais_velha = max(people, key=people.get)  


print(f"\nSoma das idades: {soma_idades}")  
print(f"Média das idades: {media_idades:.2f}")  
print(f"A pessoa mais velha é: {pessoa_mais_velha} com {people[pessoa_mais_velha]} anos.")