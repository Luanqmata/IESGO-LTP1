class Funcionario:
    def __init__(self, nome, sobrenome, idade, salario, admissao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.salario = salario
        self.admissao = admissao
    
    def salario_anual(self):
        anual = self.salario * 12
        return f' o salario anual foi de: {anual}'
    
    def aumentar_salario(self,percentual_aumento):
        self.salario += self.salario * percentual_aumento / 100
    
    def __str__(self):
        return f'Funcionario {self.nome} {self.sobrenome} , idade:{self.idade} , salario:{self.salario} , data de adimissão: { self.admissao}'

funcionario001 = Funcionario('joao','darcel', 25 , 4000 , '01/05/2019')

print(funcionario001)