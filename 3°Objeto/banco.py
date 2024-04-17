from time import sleep

class Banco:
    def __init__(self,titular,saldo =0):
        self.__titular =  titular   # encapsular dois _ _ (armazenar de forma escondida (privado))
        self.__saldo = saldo
    
    def deposito(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            return f' valor invalido '
        
    def saque(self,valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                return ' Voce nao tem saldo '
        else:
            return f' valor invalido '

    def get_saldo(self):
        return self.__saldo
    
aplica = Banco('Luan', 1000)
deposito_valor = int(input('Digite o valor do deposito: '))
aplica.deposito(deposito_valor)
print(f'O saldo atual da conta é: {aplica.get_saldo()}')