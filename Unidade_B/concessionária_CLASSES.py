class Carro:
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.vendido = False

    def infos(self):
        if self.vendido:
            return f'\n*Carro Vendido!* Temos: \n\n   Marca: {self.marca}      Modelo: {self.modelo} \n             Do ano de: {self.ano} \n             Valor: R$ {self.preco} k \n\n ---------------------------------------------- '
        else:
            return f'\n*Carro Em estoque!* Temos:\n\n   Marca: {self.marca}      Modelo: {self.modelo} \n             Do ano de: {self.ano} \n             Valor: R$ {self.preco} k\n\n---------------------------------------------- '

    def compra(self):
        self.vendido = True
    
    def ajuste_valor(self, valor_novo):
        self.preco = valor_novo

toyota = Carro("Toyota", "Mazda RX-7 Turbo", "2002", 60)
mitsubishi= Carro("Mitsubishi","Eclipse GsT 2.0 AT", "1998" , 67)
camaro_chevrolet = Carro("ChevroleT","Camaro Ss Chevelle V8 Malibu","1976", 250.0)
caravan_chevrolet = Carro("ChevroleT","Caravan Diplomata v6 Bi-Turbo","1989", 120.0)
nissan = Carro("Nissan","370s VQ V6 3.7","2012" , 219.0)

print(toyota.infos())
print(mitsubishi.infos())
print(camaro_chevrolet.infos())
print(caravan_chevrolet.infos())
print(nissan.infos())

toyota.compra()
toyota.ajuste_valor(80)

mitsubishi.ajuste_valor(95)
mitsubishi.compra()

print(toyota.infos())

print(mitsubishi.infos())

