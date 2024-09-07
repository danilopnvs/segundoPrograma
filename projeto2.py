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
            return "Abaixo do peso"
        elif 18.5 <= IMC < 24.9:
            return "Peso normal"
        elif 25 <= IMC < 29.9:
            return "Sobrepeso"
        else:
            return "Obesidade"         
    
    # Método Apresentar
    def apresentar(self):
        print("Eu sou", self.nome, "e tenho", self.idade, "anos")

    # Método Compara idade
    def compara_idade(self, idade2):
        if self.idade>idade2:
            print("Zezinho é mais velho")
        elif self.idade<idade2:
            print("Zezinho é mais novo")
        elif self.idade==idade2:
            print("Zezinho tem a mesma idade")

pessoa1 = Pessoa("Zezinho", 15, 1.53, 68.2)

print(pessoa1.eh_maior())
print(pessoa1.imc())
print(pessoa1.imc_longo())
print(pessoa1.apresentar())
print(pessoa1.compara_idade(15))
