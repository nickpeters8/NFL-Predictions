# What the file does
import pandas as pd
from IPython.display import display


def cumulative_int_stat(data_dict, team_name, week, stat_name, stat_count, current_stat_value, bye_week):
    if not bye_week:
        if current_stat_value == "":
            current_stat_value = 0
        current_stat_value = int(current_stat_value)
        stat_count += current_stat_value  ##Cumulative
    data_dict["2021"][team_name][week][stat_name] = stat_count

    return stat_count

def cumulative_float_stat(data_dict, team_name, week, stat_name, stat_count, current_stat_value, bye_week):
    if not bye_week:
        if current_stat_value == "":
            current_stat_value = 0
        current_stat_value = float(current_stat_value)
        stat_count += current_stat_value  ##Cumulative
    data_dict["2021"][team_name][week][stat_name] =  format(stat_count, '.2f')

    return stat_count


def main():
    path_prefix = "../data/Weekly stats/"
    data_csvs = ["Buffalo_Bills.csv"]

    weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6', 'Week 7', 'Week 8', 'Week 9', 'Week 10', 'Week 11', 'Week 12', 'Week 13', 'Week 14', 'Week 15', 'Week 16', 'Week 17', 'Week 18']

    data_dict = {}
    data_dict["2021"] = {}

    for csv in data_csvs:
        team_name = csv.replace(".csv", "")
        data_dict["2021"][team_name] = {}

        total_points_for = 0
        total_points_against = 0
        total_off_1st_downs = 0
        total_off_total_yards = 0
        total_off_pass_yards = 0
        total_off_rush_yards = 0
        total_off_turnovers = 0
        total_def_1st_downs = 0
        total_def_total_yards = 0
        total_def_pass_yards = 0
        total_def_rush_yards = 0
        total_def_turnovers = 0
        total_off_expected_points = 0
        total_def_expected_points = 0
        total_spt_expected_points = 0


        ##Extract data from csv file
        full_csv_path = path_prefix + csv
        f = open(full_csv_path)
        lines = f.readlines()
        lines = [row.split(",") for row in lines]

        ##Pulled out data we care about
        for idx, row in enumerate(lines):
            bye_week = False
            if idx <= 1:    ##First two lines are titles
                continue
            if row[9] == 'Bye Week':
                bye_week = True

            ##Add another dictionary for each individual week
            week_prefix = 'Week '
            week = row[0]
            week_name = week_prefix + str(week)
            data_dict["2021"][team_name][week_name] = {}

            ## Extract record from data
            record = row[7]
            if bye_week:
                data_dict["2021"][team_name][week_name]['W'] = ''
                data_dict["2021"][team_name][week_name]['L'] = ''
            else:
                record = record.split('-')
                data_dict["2021"][team_name][week_name]['W'] = int(record[0])
                data_dict["2021"][team_name][week_name]['L'] = int(record[1])

            points_for = row[10]
            total_points_for = cumulative_int_stat(data_dict, team_name, week_name, "Points For", total_points_for, points_for, bye_week)

            points_against = row[11]
            total_points_against = cumulative_int_stat(data_dict, team_name, week_name, "Points Against", total_points_against, points_against, bye_week)

            off_1st_downs = row[12]
            total_off_1st_downs = cumulative_int_stat(data_dict, team_name, week_name, "Offensive 1st Downs", total_off_1st_downs, off_1st_downs, bye_week)

            off_total_yards = row[13]
            total_off_total_yards = cumulative_int_stat(data_dict, team_name, week_name, "Offensive Total Yards", total_off_total_yards, off_total_yards, bye_week)

            off_pass_yards = row[14]
            total_off_pass_yards = cumulative_int_stat(data_dict, team_name, week_name, "Offensive Pass Yards", total_off_pass_yards, off_pass_yards, bye_week)

            off_rush_yards = row[15]
            total_off_rush_yards = cumulative_int_stat(data_dict, team_name, week_name, "Offensive Rush Yards", total_off_rush_yards, off_rush_yards, bye_week)

            off_turnovers = row[16]
            total_off_turnovers = cumulative_int_stat(data_dict, team_name, week_name, "Offensive Turnovers", total_off_turnovers, off_turnovers, bye_week)

            def_1st_downs = row[17]
            total_def_1st_downs = cumulative_int_stat(data_dict, team_name, week_name, "Defensive 1st Downs", total_def_1st_downs, def_1st_downs, bye_week)

            def_total_yards = row[18]
            total_def_total_yards = cumulative_int_stat(data_dict, team_name, week_name, "Defensive Total Yards", total_def_total_yards, def_total_yards, bye_week)

            def_pass_yards = row[19]
            total_def_pass_yards = cumulative_int_stat(data_dict, team_name, week_name, "Defensive Pass Yards", total_def_pass_yards, def_pass_yards, bye_week)

            def_rush_yards = row[20]
            total_def_rush_yards = cumulative_int_stat(data_dict, team_name, week_name, "Defensive Rush Yards", total_def_rush_yards, def_rush_yards, bye_week)

            def_turnovers = row[21]
            total_def_turnovers = cumulative_int_stat(data_dict, team_name, week_name, "Defensive Turnovers", total_def_turnovers, def_turnovers, bye_week)

            off_expected_points = row[22]
            total_off_expected_points = cumulative_float_stat(data_dict, team_name, week_name, "Offensive Expected Points", total_off_expected_points, off_expected_points, bye_week)

            def_expected_points = row[23]
            total_def_expected_points = cumulative_float_stat(data_dict, team_name, week_name, "Defensive Expected Points", total_def_expected_points, def_expected_points, bye_week)

            spt_expected_points = row[24]
            total_spt_expected_points = cumulative_float_stat(data_dict, team_name, week_name, "Special Teams Expected Points", total_spt_expected_points, spt_expected_points, bye_week)





    data_dict = pd.DataFrame.from_dict(data_dict)
    display(data_dict["2021"]["Buffalo_Bills"])


if __name__ == "__main__":
    main()
