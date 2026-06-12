"""Ejercicio 3"""

def goals_distribution(data):
    """
    Calcula la distribución de goles marcados por cada el equipo local y el visitante

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    Returns
    -------
    tuple
        distr_goals_home : pandas.DataFrame
            Número de partidos por goles marcados por el equipo local

        distr_goals_away : pandas.DataFrame
            Número de partidos por goles marcados por el equipo visitante
    """
    distr_goals_home=(
        data["FTHG"]
        .value_counts()
        .sort_index()
        .to_frame(name="Partidos")
            )
    distr_goals_away=(
        data["FTAG"]
        .value_counts()
        .sort_index()
        .to_frame(name="Partidos")
          )

    return distr_goals_home, distr_goals_away
