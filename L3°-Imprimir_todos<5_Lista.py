# Exercício 16 - Considere a seguinte lista: a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] ----> e escreva um programa que imprime todos os elementos
# da lista que são menores que 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
limite = 5

print('WHile:')
while limite >= 1:  
    print(a[limite - 1])  
    limite -= 1  


print('For:')
for i in range(4,-1,-1):
    print(a[i])
            
