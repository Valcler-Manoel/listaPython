# Explique a função map()

# A função 'map' é usada para aplicar uma determinada função a cada ‘item’ de uma sequência de elementos
# (como uma lista ou dicionário) e retorna um objeto iterável com os resultados.

#    A sintaxe padrão da função map() é:
#        map(function, iterable, [iterable 2, iterable 3, ...])
#    Em que os iterables serão aplicados as regras de function a cada iterable na expressão.


# No exemplo abaixo, utilizando o método ‘loop’ for, há uma lista
# informando 4 itens serão somados +5 em cada 'item'.

lista = [4, 1, 8, 9]  # Criado uma lista com números aleatórios.
resultado = []

for item in lista:  # Para cada ‘item’ na lista
    resultado.append(item + 8)  # será acrescentado +8.
    print(f'Lista com loop for(): {resultado}')


# No entanto, se tratando na função map() poderemos refazer o mesmo código, dessa forma:

def soma(n):  # Criado uma função soma que recebe um único argumento "n".
    return n + 8  # Retorna o valor com +8.


lista = [4, 1, 8, 9]  # Repetindo a lista.
lesultado = list(map(soma, lista))  # A função map() é aplicada usar a função soma
print(f'Lista com a função map(): {lesultado}')  # a cada elemento da lista, fazendo com que esse novo
# resultado seja armazenado como um novo objeto iterável.
