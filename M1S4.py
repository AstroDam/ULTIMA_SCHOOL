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
# criando a classe
class Clientes:
    def init(self):
        self.nome = None
        self.cpf = None
        self.idade = None

    def cadastrar(self):
        self.nome = input('informe o seu nome: \n')
        self.cpf = input('Digite os 11 digitos do seu CPF: \n')
        self.idade = int(input('informe sua idade: \n'))

    def apresentar(self): # exibindo os dados do cliente
       print(f'Nome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf} \n')

#Começa aqui
print ('OLÁ, SEJA BEM VINDO A AREA DO CLIENTE')

clientes = [] #criou lista para armazenar clientes
while True:
    toque = input('(1) Cadastre-se \n(2) Exiba seus dados \n(3) SAIR \n') #cria mnenu fora da classe, porque dentro da classe iria ficar sobrescrevendo os dados da classe
    if toque == '1':
        novo = Clientes() #instancia de objeto dentro do do 'if' para criar novos objetos sempre que houver novo cadastro
        novo.cadastrar() #chama o método cadastrar 
        clientes.append(novo) # adiciona o novo cadastro dentro da lista CLIENTES que criada fora do while
    elif toque == '2':
        for cliente in clientes: # for para rodar todos o clientes armazenados na lista
            cliente.apresentar() #chama o métodos para apresentar
    elif toque == '3':
        break
    else:
        print("Opção inválida!")

