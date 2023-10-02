''''Olá! Você foi contratado (a) como programador (a) do Ultima-Bank, o melhor banco da América Latina!

O Ultima-Bank ainda é um banco novo, então alguns processos internos ainda estão sendo realizados de maneira manual, com muita papelada envolvida!

Para agilizar os processos internos, você foi encarregado (a) de desenvolver um sistema de cadastro de novos clientes utilizando Python!

Você entregará nesta tarefa apenas um protótipo para o cadastro de 5 clientes, e caso dê certo, expandiremos para todos os milhões de clientes do Ultima-Bank.

Os dados a serem salvos são:

Nome (String)
CPF (String)
Idade (Inteiro)
Dicas:

Você pode criar uma lista para adicionar todos os clientes;
Você pode usar um dicionário para armazenar cada cliente;
Você vai obter os dados pela entrada padrão (usando a função input()).
Extra (Opcional): Desenvolver utilizando classes.
Saída do seu programa:

Você deve mostrar a seguinte mensagem para cada cliente: print("Cliente:", cliente["Nome"], "CPF:", cliente["CPF"], "Idade:", cliente["Idade"])
Por exemplo: Cliente: John Snow CPF: 963.125.345-78 Idade: 24
Mostre os cinco clientes, um após o outro.'''''

class Clientes:
    def __init__(self, nome=None, cpf=None, idade=None):
        self.__nome = nome
        self.__cpf = cpf
        self.__idade= idade

    @property
    def nome(self):
        return self.__nome
  
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome       
 
    @property
    def cpf(self):
        return self.__cpf
  
    @cpf.setter
    def cpf(self, novo_cpf):
        self.__cpf = novo_cpf  
        
    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade  
    
    def __str__(self):
        return f'A Pessoa - {self.__nome} com CPF: {self.__cpf} tem {self.__idade} anos'

cadastro = []

for i in range(1,6,1):
    
    pessoa = input('digite seu nome: ') 
    numcpf = input ('digite o seu CPF : ')
    age = input('digite sua idade: ') 
    
    ncpf = Clientes(str(pessoa),str(numcpf),str(age))

    cadastro.append(ncpf)
        
for programa in cadastro:
    print (programa)

# while True:
    
#     pessoa = input('digite seu nome: ') 
#     numcpf = input ('digite o seu CPF : ')
#     age = input('digite sua idade: ') 
    
#     ncpf = Clientes(str(pessoa),str(numcpf),str(age))

#     cadastro.append(ncpf)
        
#     if pessoa == '':
#         break
    
# for programa in cadastro:
#     print (programa)
    
        
    
   

