 
def fahrenheit_para_celsius(f):  
    return (f - 32) * 5.0/9.0  

temperaturas_fahrenheit = []  


while True:  
    entrada = input("Digite a temperatura em Fahrenheit (ou pressione Enter para sair): ")  
    if entrada == "":  
        break   
    try:  
        temperatura = float(entrada)  
        temperaturas_fahrenheit.append(temperatura)    
    except ValueError:  
        print("Por favor, insira um número válido.")  

  
temperaturas_celsius = list(map(fahrenheit_para_celsius, temperaturas_fahrenheit))  

  
print("\nTemperaturas em Celsius:")  
for c in temperaturas_celsius:  
    print(f"{c:.2f} °C")   