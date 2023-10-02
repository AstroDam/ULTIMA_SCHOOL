'''class Pessoa:
    def __init__(self, name, age): #definição da classe
        self.nome = name #atributo
        self.idade = age #atributo
    def apresentar(self): #definição de comportamento
        print(f'olá meu nome é {self.nome}')
    def criar_cadastro(self):
        print('cadastro')
pessoa01 = Pessoa('Layane', 21) #criando um objeto
pessoa01.apresentar() #objeto chamando o comportamento
pessoa01.criar_cadastro() '''

# 1. Classe Bola: Crie uma classe que modele uma bola: Atributos: Cor,
# circunferência, material
# Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def Mostra_cor(self):
        print(f'A cor da bola é {self.cor}')
        
    def Troca_cor(self, iluminacao):
        if iluminacao == 'escuro':
            print ('a bola fica florescente')
        elif iluminacao == 'claro':
            print ('a bola fica fosca')

      
        
        
bola01 = Bola('Prata', '30cm', 'borracha' )
bola01.Mostra_cor()
bola01.Troca_cor('escuro')


    
        
        
        
