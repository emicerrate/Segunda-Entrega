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


def simulate_rounds(rounds, total_stats):
    """Simula todas las rondas del juego y actualiza las estadísticas totales de los jugadores."""
    for round in rounds:
        round_scores = calculate_round_scores(round)


def final_ranking(stats):
    """Imprime el ranking final del juego."""
    return None