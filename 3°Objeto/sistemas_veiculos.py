class Veiculo:
    def __init__(self,marca,modelo,ano,valor,cor,qnt_rodas):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor
        self.qnt_rodas = qnt_rodas
    
    def __str__(self):
        return f'marca={self.marca}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}, cor={self.cor}, quantidade de rodas={self.qnt_rodas}'

    
#class Carro:
 #   def __init__(self,qnt_portas,) 

veiculo1 = Veiculo('fiat' , 'sport' , 2020 , 20000 , 'vermelho' , 4)
print(veiculo1)