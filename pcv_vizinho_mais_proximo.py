# PCV - Vizinhos mais próximos

import random


def nearest_neighbor(distance_matrix):
    n = len(distance_matrix)
    visited = [False] * n
    tour = []
    total_distance = 0

    # Escolher uma cidade inicial aleatória
    start = random.randint(0, n - 1)
    current_city = start
    visited[start] = True
    tour.append(start)

    # Enquanto nem todas as cidades forem visitadas
    while len(tour) < n:
        next_city = None
        min_distance = float('inf')

        # Procurar a cidade não visitada mais próxima
        for j in range(n):
            if not visited[j] and distance_matrix[current_city][j] < min_distance:
                next_city = j
                min_distance = distance_matrix[current_city][j]

        # Atualizar tour e distâncias
        tour.append(next_city)
        visited[next_city] = True
        total_distance += min_distance
        current_city = next_city

    # Retornar à cidade inicial
    total_distance += distance_matrix[current_city][start]
    tour.append(start)

    return tour, total_distance



# com 4 cidades:
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

rota, distancia_total = nearest_neighbor(distances)
print("Rota:", rota)
print("Distância total:", distancia_total)