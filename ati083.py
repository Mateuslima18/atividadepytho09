import random  

 
def preencher_vetor(tamanho):  
    return [random.randint(0, 20) for _ in range(tamanho)]  

  
def manipular_vetor(vetor):  
    for i in range(1, len(vetor)):  
        vetor[i] += vetor[i - 1]  

  
tamanho = 10  


vetor_original = preencher_vetor(tamanho)  
print("Vetor original:", vetor_original)  

  
manipular_vetor(vetor_original)  
print("Vetor manipulado:", vetor_original)  