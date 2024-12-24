#Соревнования по футболу между командами проводятся в два этапа. Для проведения первого этапа участники разбиваются на две группы по 12 команд.
#Для проведения второго этапа выбирается 6 лучших команд каждой группы по результатам первого этапа. Составить список команд участников второго этапа.

class Team:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __repr__(self):
        return f"{self.name} (Очки: {self.points})"


class Group:
    def __init__(self, group_name):
        self.group_name = group_name
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def get_top_teams(self, count=6):
        sorted_teams = sorted(self.teams, key=lambda t: t.points, reverse=True)
        return sorted_teams[:count]


class Tournament:
    def __init__(self):
        self.groups = []

    def add_group(self, group):

        self.groups.append(group)

    def get_final_teams(self):
        final_teams = []
        for group in self.groups:
            final_teams.extend(group.get_top_teams())
        return final_teams


def main():
    group_a = Group("Группа A")
    group_b = Group("Группа B")

    group_a.add_team(Team("Команда A1", 25))
    group_a.add_team(Team("Команда A2", 18))
    group_a.add_team(Team("Команда A3", 20))
    group_a.add_team(Team("Команда A4", 30))
    group_a.add_team(Team("Команда A5", 15))
    group_a.add_team(Team("Команда A6", 22))
    group_a.add_team(Team("Команда A7", 10))
    group_a.add_team(Team("Команда A8", 28))
    group_a.add_team(Team("Команда A9", 12))
    group_a.add_team(Team("Команда A10", 19))
    group_a.add_team(Team("Команда A11", 23))
    group_a.add_team(Team("Команда A12", 17))

    group_b.add_team(Team("Команда B1", 27))
    group_b.add_team(Team("Команда B2", 24))
    group_b.add_team(Team("Команда B3", 29))
    group_b.add_team(Team("Команда B4", 21))
    group_b.add_team(Team("Команда B5", 16))
    group_b.add_team(Team("Команда B6", 18))
    group_b.add_team(Team("Команда B7", 14))
    group_b.add_team(Team("Команда B8", 26))
    group_b.add_team(Team("Команда B9", 11))
    group_b.add_team(Team("Команда B10", 20))
    group_b.add_team(Team("Команда B11", 15))
    group_b.add_team(Team("Команда B12", 13))

    tournament = Tournament()
    tournament.add_group(group_a)
    tournament.add_group(group_b)

    final_teams = tournament.get_final_teams()

    print("Команды, прошедшие во второй этап:")
    for team in final_teams:
        print(team)


if __name__ == "__main__":
    main()

