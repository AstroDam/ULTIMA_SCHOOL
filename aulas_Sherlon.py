'''numero = int(input())
if numero % 2 == 0:
    print ("par")
else:
    print ("impar")'''

#second version
''' def p_i (numero):  
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input())
result = p_i (numero)
print (result) '''

#classe com sherlon

""" class Exe:
    #INIT é metódo contrustor. ele é executado assim que m objeto desta classe é criado (instanciado)
    def __init__(self):
        self.mensagem ="welcome"
        print ('entrou no metodo init')
    def boas_vindos(self):
        print(self.mensagem)
        
meu_objeto = Exe() #cria um objeto da classe Exe()
meu_objeto.boas_vindos()

class Pessoa:
    def __init__ (self, nome):
        self.nome = nome
        
    def welcome(self):
        print(f"you are welcome, {self.nome}")
cliente = Pessoa('daniel')
cliente.welcome() """

class Pessoa:
    def __init__ (self):
        self.nome = None
        self.idade = None
        
    def cadastro(self):
        self.nome = input("Digite o seu nome")
        self.idade = int(input("informe sua idade: "))
        
    def welcome(self):
        print(f"you are welcome, {self.nome} ({self.idade})")
meus_clientes = [] #armazenar clientes    
for iteracao in range(3):
    cliente = Pessoa()
    cliente.cadastro()
    meus_clientes.append(cliente)

meus_clientes[0].welcome()
meus_clientes[1].welcome()

'''perguntar sobre o singleton e command, adapter, strategy, facade,'''
