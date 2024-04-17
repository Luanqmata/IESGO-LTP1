"""
Objetivo: Desenvolver um programa em Python que simula um zoológico com diferentes tipos de animais, cada um com seus próprios comportamentos para emitir sons, comer e realizar uma atividade característica.



### Descrição: Você criará uma classe base chamada Animal e várias subclasses representando diferentes tipos de animais. Cada classe terá métodos para emitir_som, comer e atividade. O objetivo é demonstrar polimorfismo ao chamar esses métodos de uma lista de animais e observar comportamentos distintos.


### Classe Base Animal:
Métodos: emitir_som(), comer(), atividade()
Método __str__ para retornar uma descrição do animal.
Subclasses (Exemplos: Cachorro, Gato, Pássaro, Elefante):
Sobrescrever todos os métodos da classe base.
Adicionar um método atividade que descreve uma ação específica do animal (exemplo: Cachorro pode "buscar bola").
    """
    
class Animal:
    def __str__(self):
        return "animal"
    def emitir_som(self):
        return "Este animal emite um som."    
    def tipo_comida(self):
        return 'Este come obs:"nao sabe"'
    def atividade (self):
        return 'este animal gosta de'

class Cachorro(Animal):
    def __str__(self):
        return "Cachorro"
    
    def emitir_som(self):
        return 'Au! Au!'
    
    def tipo_comida(self):
        return 'Este cachorro gosta de osso. obs:"carnivoro"'
    
    def atividade(self):
        return 'correr no parque'

class Gato(Animal):
    def __str__(self):
        return 'Gato'
    def emitir_som(self):
        return 'MIAUUU'
    def tipo_comida(self):
        return 'Este Gato come rato. obs:"carnivoro"'
    def atividade(self):
        return 'Corre atraz de lã'

class Passaro(Animal):
    def __str__(self):
        return 'Passaro'
    def emitir_som(self):
        return 'pru! pru!'
    def tipo_comida(self):
        return 'Este passaro come Pão, obs:"Herbivaro"'
    def atividade(self):
        return 'gosta de Voar.'

class Elefante(Animal):
    def __str__(self):
        return 'Elefante.'
    def emitir_som(self):
        return 'prrurlur , prurlur'
    def tipo_comida(self):
        return 'Esse elefante come plantas. obs:"Herbivaro"'
    def atividade(self):
        return 'tomar banho de lama'

parque =[Gato(), Elefante(), Passaro(), Cachorro()]

for animal in parque:
    print(f"Animal: {animal}")
    print(f"som: {animal.emitir_som()}")
    print(f"comida: {animal.tipo_comida()}")
    print(f"atividade: {animal.atividade()}")
    print("-" * 50)
    
    
        
    
        
