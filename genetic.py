from random import getrandbits, randint, random, choice
from matplotlib import pyplot as plt

def generate_chromosome(num_items):
    return [getrandbits(1) for _ in range(num_items)]

def population(num_de_individuos, num_items):
    return [generate_chromosome(num_items) for _ in range(num_de_individuos)]

def fitness(cromossomo, peso_maximo, pesos_e_valores):
    valor_total = 0
    peso_total = 0
    
    for indice, valor in enumerate(cromossomo):
        peso_total += valor * pesos_e_valores[indice][0]
        valor_total += valor * pesos_e_valores[indice][1]

    if peso_total == 0:
        return -1  # caso todos os itens sejam excluídos

    if peso_total > peso_maximo:
        return -1  # retorna -1 no caso de peso excedido
    return valor_total  # se for um indivíduo válido, retorna seu valor (maior é melhor)


def media_fitness(populacao, peso_maximo, pesos_e_valores):
    individuos_validos = [individuo for individuo in populacao if fitness(individuo, peso_maximo, pesos_e_valores) >= 0]
    if not individuos_validos:
        return 0
    summed = sum(fitness(x, peso_maximo, pesos_e_valores) for x in individuos_validos)
    return summed / len(individuos_validos)

def selecao_roleta(pais):
    def sortear(fitness_total, indice_a_ignorar=-1):
        # O sorteio aleatório garante proporcionalidade à aptidão na seleção por roleta.
        valor_sorteado = random() if indice_a_ignorar == -1 else random() * (fitness_total - pais[indice_a_ignorar][0])
        acumulado = 0
        for indice, (fitness, _) in enumerate(pais):
            if indice == indice_a_ignorar:
                continue
            acumulado += fitness
            if acumulado >= valor_sorteado:
                return indice

    fitness_total = sum(fitness for fitness, _ in pais)

    indice_pai = sortear(fitness_total)
    indice_mae = sortear(fitness_total, indice_pai)

    pai = pais[indice_pai][1]
    mae = pais[indice_mae][1]

    return pai, mae

def gerarNovaGeracao(populacao, peso_maximo, pesos_e_valores, n_de_cromossomos, mutate=0.05):
    pais = [(fitness(x, peso_maximo, pesos_e_valores), x) for x in populacao if fitness(x, peso_maximo, pesos_e_valores) >= 0]
    pais.sort(reverse=True)

    # REPRODUCÃO
    filhos = []
    while len(filhos) < n_de_cromossomos:
        # Seleciona dois pais com base na seleção por roleta
        homem, mulher = selecao_roleta(pais)
        
        # Ponto de corte no meio dos cromossomos
        meio = len(homem) // 2
        
        # Combinação dos cromossomos dos pais para gerar um filho
        filho = homem[:meio] + mulher[meio:]

        # Adiciona o filho à lista de filhos
        filhos.append(filho)

    # Mutação: Inverte aleatoriamente um bit no cromossomo para introduzir variação genética.
    for individuo in filhos:
        if mutate > random():
            pos_to_mutate = randint(0, len(individuo) - 1)
            individuo[pos_to_mutate] ^= 1  # Operador XOR usado para inverter o bit.

    return filhos