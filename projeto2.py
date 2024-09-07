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
            return "é mais velho"
        elif self.idade<idade2:
            return "é mais novo"
        elif self.idade==idade2:
            return "tem a mesma idade"

pessoa1 = Pessoa("Zezinho", 15, 1.53, 68.2)

print(pessoa1.nome,"é maior de idade?", pessoa1.eh_maior())
print("O IMC do {} é {:.2f}".format(pessoa1.nome, pessoa1.imc()))
print("O {} está {}".format(pessoa1.nome, pessoa1.imc_longo()))
print("Quem eu sou? {}".format(pessoa1.apresentar()))


idade_referencia = 10
print ("{} tem {} anos, a segunda pessoa tem {} anos, portanto, {} {}".format(pessoa1.nome, pessoa1.idade, idade_referencia, pessoa1.nome,   pessoa1.compara_idade(idade_referencia)))
