def conversor_graus_fire_celso():
    fire = float(input('digite o grau °F: '))
    celso = (fire-32)/1.8
    valor_final = "{:.2f}".format(celso)
    return print(f"O grau Fahrenheit selecionado foi: {fire}\n Conversão: {valor_final} °Celsius.")

def conversor_graus_celso_fire():
    celsio = float(input('digite o grau °C: '))
    firehin = (1.8*celsio)+32
    valor_final2 = "{:.2f}".format(firehin)
    return print(f"O grau Celsius selecionado foi: {celsio}\n Conversão: {valor_final2} °Fahrenheit.")

selecao_user = int(input("Conversão de F°~C° digite 1. \n Conversão de C°~F° digite 2."))

if selecao_user == 1:
    conversor_graus_fire_celso()
elif selecao_user == 2:
    conversor_graus_celso_fire()
else:
    print("Digite somente entre 1 e 2.")
