class Clientes:
    def init(self):
        self.nome = None
        self.cpf = None
        self.idade = None

    def cadastrar(self):
        self.nome = input('informe o seu nome: ')
        self.cpf = input('Digite os 11 digitos do seu CPF: ')
        self.idade = int(input('informe sua idade: '))
        novo.apresentar()

    def apresentar(self): # exibindo os dados do cliente
       print(f'Nome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf} \n')

#Começa aqui
print ('OLÁ, SEJA BEM VINDO A AREA DO CLIENTE')

clientes = []
while True:
    toque = input('(1) Cadastre-se \n(2) Exiba seus dados \n(3) SAIR \n')
    if toque == '1':
        novo = Clientes() 
        novo.cadastrar()
        clientes.append(novo)
    elif toque == '2':
        for cliente in clientes:
            cliente.apresentar()
    elif toque == '3':
        break
    else:
        print("Opção inválida!")