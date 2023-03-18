numero = int(input("digite o número que deseja conferir se faz parte da sequencia: "))
esta = 'nao'

def Fibonacci(numero,esta):
    ultimo = 1
    penultimo = 1
    inicial = 1
    if (numero ==0) or (numero == 1) or (numero ==2):
        esta = "sim"
    else:
        for count in range(2,50):
            termo = ultimo + penultimo
            penultimo = ultimo
            ultimo = termo
            count += 1
            if (numero == termo):
                esta = "sim"
                break
    
    if (esta == "sim"):
        print("o número pertence a sequência!")
    else: 
        print("o número não corresponde a sequência!")
    
Fibonacci(numero, esta)
