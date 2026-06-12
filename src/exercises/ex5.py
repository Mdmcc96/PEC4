"""Ejercicio 5"""


def add_points(data):
    """
    Añade los puntos obtenidos por los equipos
    locales y visitantes en cada partido.

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos.

    Returns
    -------
    pandas.DataFrame
        Dataset con las columnas points_home
        y points_away añadidas.
    """
    
    data = data.copy()

    data["points_home"] = 0
    data["points_away"] = 0


    data.loc[data["FTR"] == "H", "points_home"] = 3
    data.loc[data["FTR"] == "D", "points_home"] = 1
    data.loc[data["FTR"] == "A", "points_home"] = 0
    data.loc[data["FTR"] == "H", "points_away"] = 0
    data.loc[data["FTR"] == "D", "points_away"] = 1
    data.loc[data["FTR"] == "A", "points_away"] = 3


    return data

def fun_total_points(data):
    """
    Calcula los puntos totales acumulados por equipo

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset con las columnas points_home y points_away

    Returns
    -------
    tuple
        total_points : pandas.Series
            Puntos totales por equipo

        df_total_points : pandas.DataFrame
            DataFrame con las columnas Team y Points
    """
    home_points = (
        data.groupby("HomeTeam")["points_home"]
        .sum()
    )
    away_points = (
        data.groupby("AwayTeam")["points_away"]
        .sum()
    )

    total_points = (
        home_points.add(
            away_points,
            fill_value=0
        )
        .sort_values(ascending=False)
    )

    df_total_points = total_points.reset_index()

    df_total_points.columns = [
        "Team",
        "Points"
    ]

    return total_points, df_total_points

def alltime_winner(df_total_points):
    """
    Obtiene el equipo con más puntos en la historia

    Parameters
    ----------
    df_total_points : pandas.DataFrame
        DataFrame de puntos totales

    Returns
    -------
    str
        Nombre del equipo ganador
    """
    winner = df_total_points.iloc[0]["Team"]

    return winner
