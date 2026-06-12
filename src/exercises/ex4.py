"""Ejercicio 4"""
import matplotlib.pyplot as plt
from exercises.config import nom_alumne, date_time
def FTR(data):
    """
    Calcula el número de victorias locales, visitantes y empates

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    Returns
    -------
    pandas.DataFrame
        DataFrame con las columnas Result y Matches
    """
   
    ftr=(
        data["FTR"]
        .value_counts()
        .sort_index()
        .reset_index()
            )
    ftr.columns =["Result","Matches"]
    return ftr

def home_win_percentage (ftr):
   """
    Calcula el porcentaje de partidos que ha ganado el equipo local

    Parameters
    ----------
    ftr : pandas.DataFrame
        DataFrame con los resultados

    Returns
    -------
    float
        Porcentaje de victorias locales
    """
   vict_loc = ftr.loc[
   ftr["Result"] == "H",
   "Matches"
   ].iloc[0]
   total_partidos = ftr["Matches"].sum()
   return (vict_loc / total_partidos) * 100

def plot_FTR(ftr):
    """
     Victorias locales, visitantes y empates representados en un diagrama de barras

    Parameters
    ----------
    ftr : pandas.DataFrame
        DataFrame con los resultados

    Returns
    -------
    matplotlib.figure.Figure
        Figura generada
            """
    fig, ax = plt.subplots(
        figsize=(8, 5)
    )

    ax.bar(
        ftr["Result"],
        ftr["Matches"]
    )

    ax.set_title(
        "Resultados finales de los partidos"
    )

    ax.set_xlabel(
        "Resultado (H, A, D)"
    )

    ax.set_ylabel(
        "Número de partidos"
    )

    plt.tight_layout()

    plt.savefig(
        f"src/img/grafica_ex4_{nom_alumne}_{date_time}.png"
    )

    plt.show()

    return fig
