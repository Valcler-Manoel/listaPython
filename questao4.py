# Reescreva o item anterior com usando for.

lista = [2, 5, 8, 11, 14]  # Criado uma lista com números aleatórios.
multiplicar = [] # Criado uma lista para ser armazenado os números multiplicados

for item in lista:  # Para cada ‘item’ na lista
    multiplicar.append(item * 2)  # será multiplicado por 2.
    print(f'Lista com loop for(): {multiplicar}') # Impressão do Resultado

maiores_10 = filter(lambda x: x > 10, multiplicar) # Utilização da função Lambda novamente para verificar
                                                   # os números maiores que 10.

print(f'Lista com números maiores que 10 {list(maiores_10)}') # Impressão dos valores > 10.