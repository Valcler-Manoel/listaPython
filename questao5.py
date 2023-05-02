# Explique o que é match: case, e como é usado no python 3.11

# A amplicação do método match: case é muito parecida com a declaração de if-else, se passando como
# um "interruptor", definindo diferentes tipos de repostas para o usuário quando as mesmas são tratadas
# como "casos", como o próprio nome da expressão diz. Porém, a mesma função ocupa menos espaço, possibilitando
# economia de espaço e mantendo um código limpo.

# Eis aqui um exemplo utilizando o match: case, simulando erros considerados comuns no mundo do HTTP.
def http_error(status):  # Definido uma função com o atributo 'status'.
    match status:
        case 400:  # Caso o valor for 400, retorne "Bad Request"
            return "Bad request"
        case 404:  # Caso o valor for 404, retorne "Not found"
            return "Not found"
        case _:  # Se nenhum dos resultados forem reconhecidos, irá informar um erro comum.
            return "Há algo errado com sua internet."


status_code = int(input("Digite um valor de status "))
print(http_error(status_code))


# Agora, ao invés de utlizar o metódo match-case, estaremos utilizando a declaração if-else no exemplo abaixo.
# É nítido a diferença de ocupamento de espaço, porém, ambos executam o mesmo código e valor.
def http_error(status):
    if status == 400: # Se o valor for 400, retorne "Bad Request"
        return "Bad request"
    elif status == 404: # Se o valor for 404, retorne "Not found"
        return "Not found"
    else:               # Se o valor não for reonhecido nos if-else, retorne uma mensagem padrão.
        return "Há algo errado com sua internet."


status_code = int(input("Enter a status code: "))
print(http_error(status_code))
