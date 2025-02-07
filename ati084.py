numeros = [1, 2, 3, 6, 7, 4, 8, 5]  

 
nova_lista = list(map(lambda x: x * 2 if x > 5 else x, numeros))  

print(nova_lista)  

quadrados = [x**2 for x in range(1, 11)]  

print(quadrados) 