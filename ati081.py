valores = []  


for i in range(5):  
    valor = int(input(f"Digite o valor {i+1} de 5: "))  
    valores.append(valor)  


x = int(input("Digite o número que deseja buscar na lista: "))  

 
if x in valores:  
    posicao = valores.index(x)  
    print(f"O valor {x} está na posição {posicao}.")  
else:  
    print(-1)  