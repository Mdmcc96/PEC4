"""Ejercicio 6"""
import pandas as pd
import matplotlib.pyplot as plt
from exercises.config import nom_alumne, date_time
def fun_total_goals(data):
    """
    Calcula el número total de goles marcados por el quipo local, visitante y el total

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    Returns
    -------
    tuple
        home_goals, away_goals, total_goals.
    """
    home_goals = int(data["FTHG"].sum())
    away_goals = int(data["FTAG"].sum())
    total_goals = home_goals + away_goals

    return home_goals, away_goals, total_goals


def fun_total_goals_by_team(data):

    """
    Calcula los goles marcados por cada equipo local, visitante y el total

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    Returns
    -------
    tuple
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team
    """
    home_goals_by_team  = (
        data.groupby("HomeTeam")["points_home"]
        .sum()
        .to_frame(name="HomeGoals")
    )
    away_goals_by_team = (
        data.groupby("AwayTeam")["points_away"]
        .sum()
        .to_frame(name="AwayGoals")
    )
    total_goals_by_team = (
        home_goals_by_team["HomeGoals"]
        .add(
            away_goals_by_team["AwayGoals"],
            fill_value=0
        )
        .to_frame(name="TotalGoals")
    )

    return (
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team
    )
def fun_summary_1996_2025(
    df_total_points_by_team,
    home_goals_by_team,
    away_goals_by_team,
    total_goals_by_team
    
):
    """
    Genera un resumen histórico sumando puntos y goles por equipo

    Returns
    -------
    pandas.DataFrame
        DataFrame resumen
    """
    summary_1996_2025 = pd.concat(
        [
            df_total_points_by_team.set_index("Team"),
            home_goals_by_team,
            away_goals_by_team,
            total_goals_by_team
        ],
        axis=1
    )

    summary_1996_2025 = (
        summary_1996_2025
        .sort_values(
            by="Points",
            ascending=False
        )
    )

    return summary_1996_2025

def podium(summary_1996_2025):
    """
    Genera una gráfica tipo podium con los tres equipos con más puntos históricos

    Parameters
    ----------
    summary_1996_2025 : pandas.DataFrame

    Returns
    -------
    matplotlib.figure.Figure
    """

    top3 = summary_1996_2025.head(3)

    first = top3.iloc[0]
    second = top3.iloc[1]
    third = top3.iloc[2]

    positions = [0, 1, 2]

    heights = [
        second["Points"],
        first["Points"],
        third["Points"]
    ]

    teams = [
        top3.index[1],
        top3.index[0],
        top3.index[2]
    ]

    fig, ax = plt.subplots(figsize=(8, 6))

    bars = ax.bar(
        positions,
        heights
    )

    ax.set_xticks([])
    ax.set_yticks([])

    for bar, team in zip(bars, teams):
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 50,
            team,
            ha="center"
        )

    ax.set_title(
        "Podium histórico LaLiga"
    )

    plt.tight_layout()

    plt.savefig(
        f"src/img/grafica_ex6_{nom_alumne}_{date_time}.png"
    )

    plt.show()

    return fig
