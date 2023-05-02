# Para quê serve a palavra reservada “assert”?

# É usada principalmente no debug de um código, verificando o valor de uma condição dada. Caso o valor
# for igual à condição, nada acontece, continuando a execução do código normalmente, porém, se o mesmo for diferente,
# retornará uma exceção 'AssertionError', quebrando o código. Em resumo, o assert tem a função de confirmar
# a credibilidade de uma função no código, caso o contrário, a execução será interrompida.

def dividir(n, d):
    assert d != 0, "Impossível dividir por 0" # Informando um assert para confirmar que o valor não pode ser
                                              # igual a 0. Retornando 'AssertionError; Impossível dividir por 0"
    return n / d


n = int(input("Numerador: "))
d = int(input("Denominadorr: "))

print(dividir(n, d))
