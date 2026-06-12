"""Ejercicio 7"""
import networkx as nx
import matplotlib.pyplot as plt
from exercises.config import nom_alumne, date_time
def graf(data, selected_teams):
    """
    Genera un grafo de conexiones entre los equipos mostrando el número de partidos disputados entre ellos

    Parameters
    ----------
    data : pandas.DataFrame
        Dataset de partidos

    selected_teams : list
        Lista con los equipos seleccionados

    Returns
    -------
    matplotlib.figure.Figure
        Figura generada
    """

    filtered_data = data[
        (data["HomeTeam"].isin(selected_teams))
        &
        (data["AwayTeam"].isin(selected_teams))
    ]

    connections = (
        filtered_data
        .groupby(["HomeTeam", "AwayTeam"])
        .size()
        .reset_index(name="Matches")
    )

    graph = nx.Graph()

    for team in selected_teams:
        graph.add_node(team)

    for _, row in connections.iterrows():

        home = row["HomeTeam"]
        away = row["AwayTeam"]
        matches = row["Matches"]

        if graph.has_edge(home, away):
            graph[home][away]["weight"] += matches
        else:
            graph.add_edge(
                home,
                away,
                weight=matches
            )

    fig, ax = plt.subplots(figsize=(10, 8))

    pos = nx.spring_layout(
        graph,
        seed=42
    )

    nx.draw_networkx(
        graph,
        pos,
        ax=ax,
        with_labels=True
    )

    edge_labels = nx.get_edge_attributes(
        graph,
        "weight"
    )

    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=edge_labels,
        ax=ax
    )

    plt.title(
        "Conexiones entre equipos históricos"
    )

    plt.axis("off")

    plt.savefig(
        f"src/img/grafica_ex7_{nom_alumne}_{date_time}.png"
    )

    plt.show()

    return fig
