  
def soma_tuplas(lista_tuplas):  
    return [sum(tupla) for tupla in lista_tuplas]  

 
lista1 = [(1, 2), (2, 3), (3, 4)]  
lista2 = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]  

  
soma1 = soma_tuplas(lista1)  
soma2 = soma_tuplas(lista2)  

  
print("Soma de todos os elementos de cada tupla na primeira lista:", soma1)  
print("Soma de todos os elementos de cada tupla na segunda lista:", soma2)  