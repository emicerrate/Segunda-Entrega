def initialize_stats(rounds):
    """Inicializa las estadísticas para cada jugador en el juego."""
    return {player: {"kills": 0, "assists": 0, "deaths": 0, "MVPs": 0, "points": 0} for player in rounds[0].keys()}


def calculate_score(kills, assists, deaths):
    """Retorna el puntaje de un jugador dadas sus estadísticas."""
    return kills * 3 + assists - (1 if deaths else 0)


def calculate_round_scores(round):
    """Retorna un diccionario de los jugadores con sus puntos ordenados por el puntaje de mayor a menor."""
    # Creo el diccionario donde almacenamos a los jugadores con sus respectivos puntos por comprensión
    scores = {player: calculate_score(stats["kills"], stats["assists"], stats["deaths"]) for player, stats in round.items()}
    
    # Uso sorted para ordenar el diccionario por los puntos de mayor a menor
    # Como sorted retorna una lista la convierto a un diccionario explicítamente
    return dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))


def mvp(round_scores):
    """Retorna el nombre del mvp de una ronda."""
    return max(round_scores, key=round_scores.get)


def print_round_scores(round, round_scores, round_number):
    """Imprime los resultados de una ronda ordenados por el puntaje de los jugadores de mayor a menor."""
    print(f"Ranking ronda {round_number}:\nJugador    Kills    Asistencias  Muertes  Puntos")
    print("-" * 56)
    for player in round_scores.keys():
        print(f"{player:8} {round[player]['kills']:3} {round[player]['assists']:8} {round[player]['deaths']:12} {round_scores[player]:8}")
    print(f"{'-' * 56}\n¡{mvp(round_scores)} es el MVP de la ronda {round_number}!\n")


def simulate_rounds(rounds, total_stats):
    """Simula todas las rondas del juego y actualiza las estadísticas totales de los jugadores."""
    # Uso enumerate para asignarle a cada ronda su respectivo número
    for i, round in enumerate(rounds):
        round_scores = calculate_round_scores(round)
        print_round_scores(round, round_scores, i+1)



def final_ranking(stats):
    """Imprime el ranking final del juego."""
    return None