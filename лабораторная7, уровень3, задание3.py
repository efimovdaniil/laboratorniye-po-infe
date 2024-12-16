#В соревнованиях участвуют три команды по 6 человек. Результаты соревнований представлены в виде мест участников каждой команды (1 - 18).
# Определить команду-победителя, вычислив количество баллов, набранное каждой командой. Участнику, занявшему 1-е место, начисляется 5 баллов, 2-е - 4, 3-е - 3, 4-е - 2, 5-е - 1, остальным - 0 баллов.
# При равенстве баллов победителем считается коман-да, за которую выступает участник, занявший 1-е место.

class Participant:
    def __init__(self, position):
        self.position = position

    def get_team_index(self):
        return (self.position - 1) // 6

    def get_place_in_team(self):
        return self.position - (self.get_team_index() * 6)


class Team:
    def __init__(self, team_number):
        self.team_number = team_number
        self.score = 0

    def add_score(self, points):
        self.score += points


class Competition:
    def __init__(self):
        self.teams = [Team(i + 1) for i in range(3)]

    def calculate_scores(self, positions):
        points = {1: 5, 2: 4, 3: 3, 4: 2, 5: 1}

        for pos in positions:
            participant = Participant(pos)
            team_index = participant.get_team_index()
            place_in_team = participant.get_place_in_team()

            if place_in_team in points:
                self.teams[team_index].add_score(points[place_in_team])

    def determine_winner(self):
        max_score = max(team.score for team in self.teams)
        winning_teams = [team for team in self.teams if team.score == max_score]
        if len(winning_teams) > 1:
            for pos in positions:
                participant = Participant(pos)
                if participant.get_place_in_team() == 1:
                    return winning_teams[participant.get_team_index()]

        return winning_teams[0]


def main():
    global positions

    positions = []
    print("Введите места участников (1-18), разделяя пробелами:")
    input_positions = input().strip().split()

    positions = [int(pos) for pos in input_positions]

    if len(positions) != 18:
        print("Ошибка: должно быть введено ровно 18 мест участников.")
        return

    competition = Competition()
    competition.calculate_scores(positions)
    winning_team = competition.determine_winner()

    print(f"Команда-победитель: Команда {winning_team.team_number} с {winning_team.score} баллами.")
    for team in competition.teams:
        print(f"Команда {team.team_number}: {team.score} баллов")


if __name__ == "__main__":
    main()
