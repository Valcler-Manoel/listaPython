# Implemente um exemplo de uso de função Lambda.

# A função Lambda abre um novo caminho na criação de funções em Python, a partir dela é possível
# criar classes invisíveis, ou seja, anônimas, sem ter a necessidade de nomeá-las. Essas novas
# modalidades de classe são importantes num planejamento de um código. Quando formos utilizar apenas
# 1 tipo de classe, e que a mesma não será utilizada no resto do código inteiro, podemos usar a funçao Lambda
# para resolver situações como essa.

# No seguinte código, é implementado a função Lambda na função map()
numeros = [2, 5, 8, 11, 14] # Declarado uma lista
multiplicar = list(map(lambda x: x*2, numeros)) # É utilizado a função 'map' para que a função 'lambda'
                                                # seja aplicada em cada 'item' da lista, armazenado
                                                # num novo objeto iterável.
print(multiplicar)

maiores_10 = filter(lambda x: x > 10, multiplicar) # É aplicado a função 'filter', numa condição
                                                   # para verificar o iterável que foi salvo,
                                                   # anteriormente, em que, se o valor for maior que 10,
                                                   # ele retornará e multiplicará por 2.
print(list(maiores_10))