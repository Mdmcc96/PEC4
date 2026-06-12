"""Ejercicio 1."""
import pandas as pd
import matplotlib.pyplot as plt
from exercises.config import nom_alumne, date_time

def load_and_eda(file):

    """
    Carga el dataset y devuelve la información

    Parameters
    ----------
    file : str
        Ruta al CSV

    Returns
    -------
    tuple
        Dataset procesado, primeras filas
        últimas filas e información general
    """

    data=pd.read_csv(file)

    columns_to_drop = ["HTHG", "HTAG", "HTR"]
    data=data.drop(columns=columns_to_drop)
    head_data=data.head()
    tail_data=data.tail()

    info_data = {
    "shape": data.shape,
    "columns": list(data.columns),
    "missing_values": data.isnull().sum()
    }
    return data, head_data, tail_data, info_data

def plot_home_away_goals(data):

    """
    Distribución de goles marcados por el equipo local y visitante usando diagramas de caja

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    Returns
    -------
    matplotlib.figure.Figure
        Figura generada
    """
    fig,axs =plt.subplots (1,2, figsize=(15, 5))

    axs[0].boxplot (data ["FTHG"])
    axs[0].set_title ('Goles equipo local')
    axs[0].set_ylabel('Goles')

    axs[1].boxplot (data["FTAG"])
    axs[1].set_title ('Goles equipo visitante')
    axs[1].set_ylabel('Goles')

    plt.tight_layout()

    plt.savefig(
        f"src/img/grafica_ex1_{nom_alumne}_{date_time}.png"
    )
    plt.show()
    return fig