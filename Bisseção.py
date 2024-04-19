import math

def bissecao(funcao, a, b, precisao):
    if funcao(a) * funcao(b) >= 0:
        print("A função não muda de sinal no intervalo dado.")
        return None, None, None

    iteracoes = 0
    while (b - a) / 2 > precisao:
        c = (a + b) / 2
        if funcao(c) == 0:
            return c, funcao(c), iteracoes
        elif funcao(c) * funcao(a) < 0:
            b = c
        else:
            a = c
        iteracoes += 1
        print(f"Iteração {iteracoes}: x = {c}")

    print(f"Iteração {iteracoes + 1}: x = {(a + b) / 2}")  # Imprime o último valor de c
    return (a + b) / 2, funcao((a + b) / 2), math.ceil(iteracoes)


# Função para avaliar f(x) em todos os pontos do intervalo
def avaliar_funcao_intervalo(funcao, a, b):
    resultados = {}
    for x in range(int(a), int(b)+1):
        resultados[x] = funcao(x)
    return resultados

# Exemplo de função
def funcao_exemplo(x):
    return x**3 - 2*x - 5

# Pedindo entrada do usuário
expressao = input("Digite a função (utilize 'x' como variável): ")
funcao_usuario = lambda x: eval(expressao)

a = float(input("Digite o limite inferior do intervalo: "))
b = float(input("Digite o limite superior do intervalo: "))
precisao = float(input("Digite a precisão desejada: "))

# Avaliar f(x) em todos os pontos do intervalo
valores_funcao = avaliar_funcao_intervalo(funcao_usuario, a, b)

# Imprimir os valores de f(x) para cada ponto dentro do intervalo
print("Valores de f(x) para cada ponto dentro do intervalo dado:")
for x, fx in valores_funcao.items():
    print(f"f({x}) = {fx}")

# Encontrar os intervalos onde ocorre mudança de sinal
pontos = sorted(valores_funcao.keys())
intervalos = []
for i in range(len(pontos)-1):
    if valores_funcao[pontos[i]] * valores_funcao[pontos[i+1]] < 0:
        intervalos.append((pontos[i], pontos[i+1]))

# Aplicar o método da bisseção em cada intervalo com mudança de sinal
resultados = []
for intervalo in intervalos:
    resultado_x, resultado_fx, iteracoes = bissecao(funcao_usuario, intervalo[0], intervalo[1], precisao)
    resultados.append((resultado_x, resultado_fx, iteracoes))

# Imprimir os resultados
print("\nResultados da análise de bisseção:")
for i, resultado in enumerate(resultados):
    print(f"Intervalo {i+1}: x = {resultado[0]}, f(x) = {resultado[1]}, Número de Iterações = {resultado[2]}")
