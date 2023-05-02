#Explique como utilizar tratamento de exceção, demonstre através
#de um código onde vai quebrar intencionalmente.

# Tratamento de exceções consiste em uma boa prática na manutenção de erros na programação,
# fazendo com que o código seja iniciado com uma certa fluidez sem a presença de erros que podem ocorrer
# durante o run do código. Por exemplo, se declararmos uma variável de tal valor, em que nela há um input
# que somente aceite valores inteiros, caso coloquemos uma valor do tipo string, o código normalmente iria
# quebrar logo em seguida. No entanto, com o tratamento de exceções, você pode tratar essa exceção usando
# a cláusula except ValueError: Isso permite que o programa continue funcionando mesmo quando ocorrem er-
# ros inesperados.

# No seguinte exemplo, trataremos algumas exceções no código.

try: #Inserido um bloco try, permitindo que existam exceções dentro do código.
    a = [1, 2, 3] #Index de 0 a 2
    value = a[3] #Pedindo para acessar o index no valor de 3, porém o mesmo não existe.
except IndexError: #Inserindo uma exceção de que, caso haja uma invalidação no erro do valor
                   #do index, o mesmo seja coletado executando a declaração seguinte.
        print("Index não existe")#Declaração sendo executada por não haver um index existente.


# Demonstrando um exemplo onde haverá uma quebra no código por não haver tratamento de exceções

x = int(input('Digite um número: ')) # Caso o usuário digite um valor diferente de um número inteiro,
                                          # o código quebrará informando um erro de ValueError
print (f'O número escolhido foi: {x}')

# Correção do código:
try:
    n = int(input('"Teste: Experimente colocar um valor não inteiro" - Digite um número: '))
    print(f'O número escolhido foi: {n}')
except ValueError: #Tratando uma excecão do tipo ValueError.
    print('Erro: informe um número inteiro!')