''' 1. Faça um programa que recebe três números do usuário, e identifica o maior através
de uma função e o menor número através de outra função.
2. Faça um script que recebe um inteiro n e mostra todos os primos, de 1 até n.
3. Faça um programa, com uma função que necessite de três argumentos, e que forneça a
soma desses três argumentos através de uma função. Seu script também deve fornecer a
média dos três números, através de uma segunda função que chama a primeira.
4. Escreva um script que pergunta ao usuário se ele deseja converter uma temperatura de
grau Celsius para Fahrenheit ou vice-versa. Para cada opção, crie uma função. Crie uma
terceira, que é um menu para o usuário escolher a opção desejada, onde esse menu chama
a função de conversão correta.
5. A série de Fibonacci é uma sequência de números, cujos dois primeiros são 0 e 1. O
termo seguinte da sequência é obtido somando os dois anteriores. Faça um script em
Python que solicite um inteiro positivo ao usuário, n. Então, uma função exibe todos os
termos da sequência até o n-ésimo termo. Use recursividade.
6. Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado
7. Faça um programa, com uma função que necessite de um argumento. A função
retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento
for zero ou negativo.'''

# exercicio 1
#def maior(x,y,z):
#    max = x

#    if y > max:
#        max = y
#    if z > max:
#        max = z

#   return max

#def menor(x,y,z):
#    min = x

#    if y < min:
#        min = y
#    if z < min:
#        min = z

#    return min

#def menu():
#    x = int(input('Primeiro numero: '))
#    y = int(input('Segundo numero : '))
#    z = int(input('Terceiro: numero: '))

#    print("Maior: ", maior(x,y,z))
#    print("Menor: ", menor(x,y,z))
#    print()
    
#while True:
#menu()
#exemplo ISAlove 1
#quantidade = 0
#lista = []
#while quantidade < 3:
#    x = int(input('digite um número: '))
#    lista.append (x)
#    quantidade += 1
#print (max (lista))
#print (min (lista))
# exercicio 4
#def menu ():
#    print ('Olá, deseja fazer conversão de temperaturas?')
#    options = input('1 - converter para celsius \n 2 - converter para fahrenheit \n 3 - sair\n')
#    if options == '1': 
#        celsius_fahrenheit()
#    elif options == '2':
#        fahrenheit_celsius()
#    else :
#        sair()
#def celsius_fahrenheit ():
#    TC = float(input(' Informe a temperatura em graus celsius: '))
#    TF = TC * 1.8 + 32
#    print('Valor em Fahrenheit: {0}°F'.format(TF))
#    menu()
#def fahrenheit_celsius ():
#    TF = float(input(' Informe a temperatura em graus celsius: '))
#    TC = (TF - 32) * 1.8
#    print('Valor em Fahrenheit: {0}°C'.format(TC))
#    menu()
#def sair():
#    print ('saindo...')
#    quit()
#menu()
# exercicio 3 
  
#def somatorio (a,b,c):
#    soma = a + b + c    
#    return soma 

#def media_somatorio(a,b,c):
#    som = a + b + c
#    media = som / 3
#    return media

#a = int(input('insira o primeiro valor a ser calculado: '))
#b = int(input('insira o segundo valor a ser calculado: '))
#c = int(input('insira o terceiro valor a ser calculado: '))
#print ('soma: ', somatorio(a,b,c)) 
#print ('media: ', media_somatorio (a,b,c))

'''exercio 6
#cont = 0
#palavra = input('digite uma palavra: ')
#for batata in palavra : 
#    cont +=1
#print (cont)

def Qualtamanho(x):
    n = str(x)
    if len(n) > 1:
        if n[0] == '0':
            return len(n) - 1
        else:
            return len(n)
    return len(n)


num = int(input("Digite um número: "))
print(Qualtamanho(num))'''


# exerecio 7
# def positivo_negativo (n1) :
    #n1 = int(input('insira uma valor: ')) 
     
#    if n1 > 0 :
 #       print ('P')
  #  else :
   #     print ("N") 
        
        
#n1 = int(input('insira uma valor: '))   

#positivo_negativo (n1)

#exercicio 5

def fibonacci(n, ultimo, penultimo, termo): 
    if (n==1) or (n==2):
        print("1")
    else:
        cont=0
    while cont < n:
        print (' >', termo, end='')
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        cont += 1
    print(' > FIM') 

n = int(input("Quantos termos você quer encontrar: "))
ultimo=0
penultimo=1
termo=0
fibonacci(n, ultimo, penultimo, termo)