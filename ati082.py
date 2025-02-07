import random  

  
lancamentos = []  

 
for _ in range(50):  
    lancamentos.append(random.randint(1, 6))  

  
contador_seis = lancamentos.count(6)  


percentual_seis = (contador_seis / 50) * 100  

  
print(f"Lançamentos: {lancamentos}")  
print(f"Número de vezes que a face 6 apareceu: {contador_seis}")  
print(f"Percentual de ocorrências da face 6: {percentual_seis:.2f}%")  