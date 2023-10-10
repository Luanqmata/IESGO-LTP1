def area_retagulo(a,b):
    formula = a * b 
    # a = comprimeto b = Largura
    print(f'A area do retagulo é de: {formula} metros/centimentros.')
    
print('CALCULA AREA RETANGULO.\n')    
comprimento_dado_user = float(input('Digite o comprimento do Retangulo: '))
largura_dado_user = float(input('Digite a Largura do Retangulo :'))

area_retagulo(comprimento_dado_user,largura_dado_user)
