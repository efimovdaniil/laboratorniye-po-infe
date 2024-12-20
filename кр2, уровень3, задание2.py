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

    print("Введите команды для Группы A:")
    for i in range(12):
        name = input(f"Введите имя команды A{i + 1}: ")
        points = int(input(f"Введите количество очков для команды {name}: "))
        group_a.add_team(Team(name, points))

    print("\nВведите команды для Группы B:")
    for i in range(12):
        name = input(f"Введите имя команды B{i + 1}: ")
        points = int(input(f"Введите количество очков для команды {name}: "))
        group_b.add_team(Team(name, points))

    tournament = Tournament()
    tournament.add_group(group_a)
    tournament.add_group(group_b)

    final_teams = tournament.get_final_teams()

    print("\nКоманды, прошедшие во второй этап:")
    for team in final_teams:
        print(team)


if __name__ == "__main__":
    main()
