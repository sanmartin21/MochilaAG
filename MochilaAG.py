from genetic import *

pesos_e_valores = [[5, 20], [10, 5], [8, 25], [30, 70], [3, 15], [60, 120], [7, 250], [15, 40], [120, 450], [10, 350]]
peso_maximo = 120
n_de_cromossomos = 200
geracoes = 100
n_de_itens = len(pesos_e_valores)

populacao = population(n_de_cromossomos, n_de_itens)
historico_de_fitness = [media_fitness(populacao, peso_maximo, pesos_e_valores)]

for i in range(geracoes):
    populacao = gerarNovaGeracao(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos)
    historico_de_fitness.append(media_fitness(populacao, peso_maximo, pesos_e_valores))

# Imprimir e plotar resultados
for indice, dados in enumerate(historico_de_fitness):
    print("Geracao: ", indice, " | Media de valor na mochila: ", dados)

print("\nPeso maximo:", peso_maximo, "g\n\nItens disponiveis:")
for indice, i in enumerate(pesos_e_valores):
    print("Item ", indice + 1, ": ", i[0], "g | R$", i[1])

print("\nMelhores soluções encontradas:")
for i in range(5):
    print("Indivíduo", i + 1, ":", populacao[-1][i])

# Plotagem
plt.plot(range(len(historico_de_fitness)), historico_de_fitness)
plt.grid(True, zorder=0)
plt.title("Problema da mochila")
plt.xlabel("Geracão")
plt.ylabel("Valor médio da mochila")
plt.show()