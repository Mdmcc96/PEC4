"""Ejercicio 2"""
import matplotlib.pyplot as plt
from exercises.config import nom_alumne, date_time
def total_matches(data):

    """
    Calcula el número total de partidos jugados
    por cada equipo durante en cada temporada

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    Returns
    -------
    pandas.DataFrame
        DataFrame con las columnas Team y Matches
    """

    equipo_local=data["HomeTeam"].value_counts()
    equipo_visit=data["AwayTeam"].value_counts()

    matches_team_total =(
        equipo_local.add(equipo_visit, fill_value=0)
        .astype(int)
        .reset_index()
    )

    matches_team_total.columns=["Team", "Matches"]

    return matches_team_total
def plot_matches_team_total(matches_team_total):

    """
    Número total de partidos jugados por cada equipo.

    Parameters
    ----------
    matches_team_total : pandas.DataFrame
        DataFrame con el número de partidos
        por equipo

    Returns
    -------
    matplotlib.figure.Figure
        Figura generada
    """
    fig,ax =plt.subplots (figsize=(12, 5))

    ax.bar(
    matches_team_total["Team"],
    matches_team_total["Matches"]
    )

    ax.set_xlabel("Equipos")
    ax.set_title ('Total partidos por equipo')
    ax.set_ylabel('Partidos')


    plt.tight_layout()
    plt.xticks(rotation=90)

    plt.savefig(
        f"src/img/grafica_ex2_{nom_alumne}_{date_time}.png"
    )
    plt.show()
    return fig
