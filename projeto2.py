class Pessoa:
    # Construtor da classe 
    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    # Médoto maior de idade
    def eh_maior(self):
        return self.idade >=18
    
    # Método IMC
    def imc(self):
        return self.peso/(self.altura*self.altura)
        
    # Método IMC longo
    def imc_longo(self):
        IMC = self.peso/(self.altura*self.altura)
        if IMC < 18.5:
            return "abaixo do peso"
        elif 18.5 <= IMC < 24.9:
            return "com o peso normal"
        elif 25 <= IMC < 29.9:
            return "em sobrepeso"
        else:
            return "com obesidade"         
    
    # Método Apresentar
    def apresentar(self):
        return ("Eu sou {} e tenho {} anos".format(self.nome, self.idade))
    
    # Método Compara idade
    def compara_idade(self, idade2):
        if self.idade>idade2:
            return "é mais velho(a)"
        elif self.idade<idade2:
            return "é mais novo(a)"
        elif self.idade==idade2:
            return "tem a mesma idade"

# Função mostrar dados
def mostrarDados(pessoa):
    print ("---------------------------------------------------------------------------------------")
    print(pessoa.nome,"é maior de idade?", pessoa.eh_maior())
    print("O IMC do {} é {:.2f}".format(pessoa.nome, pessoa.imc()))
    print("O {} está {}".format(pessoa.nome, pessoa.imc_longo()))
    print("Quem eu sou? {}".format(pessoa.apresentar()))
    idade_referencia = int(input ("Digite a idade de uma segunda pessoa: "))
    print ("{} tem {} anos, a segunda pessoa tem {} anos, portanto, {} {}".format(pessoa.nome, pessoa.idade, idade_referencia, pessoa.nome,   pessoa.compara_idade(idade_referencia)))
    print ("---------------------------------------------------------------------------------------")

pessoa1 = Pessoa("Zezinho", 15, 1.53, 68.2)
mostrarDados(pessoa1)

pessoa2 = Pessoa("João", 31, 1.73, 92.2)
mostrarDados(pessoa2)

pessoa3 = Pessoa("Maria", 26, 1.72, 70.8)
mostrarDados(pessoa3)

