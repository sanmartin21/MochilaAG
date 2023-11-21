from genetic import *
import matplotlib.pyplot as plt

# Definindo os dados
pesos_e_valores = [[5, 20], [10, 5], [8, 25], [30, 70], [3, 15], [60, 120], [7, 250], [15, 40], [120, 450], [10, 350]]
peso_maximo = 120
n_de_cromossomos = 200
geracoes = 100
n_de_itens = len(pesos_e_valores)

# Inicializando a população
populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]

# Gerando novas gerações
for i in range(geracoes):
    populacao = gerarNovaGeracao(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

# Função para imprimir os resultados
def imprimir_resultados(historico_de_fitness, populacao):
    print("\nResultados:\n")
    for indice, dados in enumerate(historico_de_fitness):
        print(f"Geracao {indice}: Media de valor na mochila = {dados}")
    print("\nExemplos de boas soluções:")
    for i in range(5):
        print(f"Indivíduo {i + 1}: {populacao[i]}")

# Imprimir os resultados
imprimir_resultados(historico_de_fitness, populacao)

# Plotagem
plt.figure(figsize=(10, 6))
plt.plot(range(len(historico_de_fitness)), historico_de_fitness, marker='1')
plt.grid(True, zorder=0)
plt.title("Evolução do valor médio da mochila ao longo das gerações")
plt.xlabel("Geracão")
plt.ylabel("Valor médio da mochila")
plt.show()
