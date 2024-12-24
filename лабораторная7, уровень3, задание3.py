#В соревнованиях участвуют три команды по 6 человек. Результаты соревнований представлены в виде мест участников каждой команды (1 - 18).
# Определить команду-победителя, вычислив количество баллов, набранное каждой командой. Участнику, занявшему 1-е место, начисляется 5 баллов, 2-е - 4, 3-е - 3, 4-е - 2, 5-е - 1, остальным - 0 баллов.
# При равенстве баллов победителем считается коман-да, за которую выступает участник, занявший 1-е место.

class Team:
    def __init__(self, name, members_positions):
        self.name = name
        self.members_positions = members_positions
        self.score = self.calculate_score()

    def calculate_score(self):
        score = 0
        for position in self.members_positions:
            if position == 1:
                score += 5
            elif position == 2:
                score += 4
            elif position == 3:
                score += 3
            elif position == 4:
                score += 2
            elif position == 5:
                score += 1
        return score


class Competition:
    def __init__(self):
        self.teams = []

    def add_team(self, team):
        self.teams.append(team)

    def determine_winner(self):

        sorted_teams = sorted(self.teams, key=lambda t: (t.score, t.members_positions[0]), reverse=True)
        return sorted_teams[0]



if __name__ == "__main__":
    team_a = Team("Команда A", [1, 4, 5, 6, 7, 8])  # 1-е место, 4-е, 5-е и т.д.
    team_b = Team("Команда B", [2, 3, 6, 8, 9, 10]) # 2-е место, 3-е и т.д.
    team_c = Team("Команда C", [3, 1, 5, 7, 11, 12]) # 3-е место, 1-е и т.д.

    competition = Competition()
    competition.add_team(team_a)
    competition.add_team(team_b)
    competition.add_team(team_c)

    winner = competition.determine_winner()

    print(f"Победитель: {winner.name} с {winner.score} баллами.")
