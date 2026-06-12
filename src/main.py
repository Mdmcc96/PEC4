import argparse
from exercises.ex1 import load_and_eda, plot_home_away_goals
from exercises.ex2 import total_matches, plot_matches_team_total
from exercises.ex3 import goals_distribution
from exercises.ex4 import FTR, plot_FTR, home_win_percentage
from exercises.ex5 import add_points, fun_total_points, alltime_winner
from exercises.ex6 import fun_total_goals, podium, fun_summary_1996_2025, fun_total_goals_by_team
from exercises.ex7 import graf

def main():
    parser = argparse.ArgumentParser(
        description="PEC4 LaLiga"
    )

    parser.add_argument(
        "-ex",
        type=int,
        default=7,
        help="Ejecuta los ejercicios hasta el número indicado"
    )

    args = parser.parse_args()

    data, head_data, tail_data, info_data = load_and_eda(
        "src/data/LaLiga_Matches.csv"
    )
    if args.ex >= 1:

        print("Primeras filas:")
        print(head_data)

        print("\nÚltimas filas:")
        print(tail_data)
        print("\nInformación:")
        print(info_data)
        plot_home_away_goals(data)
    if args.ex >= 2:
        matches_team_total = total_matches(data)

        print(matches_team_total.head(10))
        max_matches = matches_team_total["Matches"].max()

        primera_division = matches_team_total[
        matches_team_total["Matches"] == max_matches
        ]

        print(primera_division)
    

        plot_matches_team_total(matches_team_total)
    if args.ex >= 3:
        distr_goals_home, distr_goals_away = goals_distribution(data)
        print(distr_goals_home)
        print(distr_goals_away)
    if args.ex >= 4:
        ftr =FTR(data)
        print(ftr)
        plot_FTR(ftr)
        porcentaje_locales=home_win_percentage(ftr)
        print(
        f"Porcentaje victorias locales: "
        f"{ porcentaje_locales:.2f}%",
        )
    if args.ex >= 5:
        data = add_points(data)
        print(data.head(10))
        total_points, df_total_points = (
        fun_total_points(data)
        )
        print(df_total_points.head(10))
        winner = alltime_winner(df_total_points)
        print(F"Ganador histórico: {winner}")

    if args.ex >= 6:
        home_goals, away_goals, total_goals = (
        fun_total_goals(data)
    )
        print(
        home_goals,
        away_goals,
        total_goals
    )
    
        home_goals_by_team, away_goals_by_team, total_goals_by_team = (
        fun_total_goals_by_team(data)
)
        print(total_goals_by_team.head(10))
        data = add_points(data)
        total_points_by_team, df_total_points = fun_total_points(data)
        summary_1996_2025 = fun_summary_1996_2025(
        df_total_points,
        home_goals_by_team,
        away_goals_by_team,
        total_goals_by_team
    )

        podium(summary_1996_2025)
    if args.ex >= 7:
        selected_teams = (
        df_total_points["Team"]
        .head(5)
        .tolist()
    )
        graf(
            data,
            selected_teams
    )
if __name__ == "__main__":
    main()