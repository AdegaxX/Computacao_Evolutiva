# PCV - Inserção mais barata

import random

def cheapest_insertion(distance_matrix):
    n = len(distance_matrix)
    unvisited = set(range(n))
    tour = []

    # Escolher duas cidades iniciais aleatórias
    start = random.choice(list(unvisited))
    unvisited.remove(start)
    second_city = random.choice(list(unvisited))
    unvisited.remove(second_city)

    # Inicializar o tour com as duas cidades e voltar ao início
    tour = [start, second_city, start]

    # Repetir até todas as cidades serem inseridas
    while unvisited:
        best_increase = float('inf')
        best_city = None
        best_position = None

        # Verificar todas as cidades não visitadas
        for city in unvisited:
            for i in range(len(tour) - 1):
                a = tour[i]
                b = tour[i + 1]
                increase = (distance_matrix[a][city] + distance_matrix[city][b] - distance_matrix[a][b])

                if increase < best_increase:
                    best_increase = increase
                    best_city = city
                    best_position = i + 1

        # Inserir a melhor cidade na melhor posição
        tour.insert(best_position, best_city)
        unvisited.remove(best_city)

    # Calcular a distância total do tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i]][tour[i + 1]]

    return tour, total_distance



# para 4 cidades:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

rota, distancia_total = cheapest_insertion(distances)
print("Rota:", rota)
print("Distância total:", distancia_total)