#Протокол соревнований по прыжкам в воду содержит список фамилий спортсменов и баллы, выставленные 5 судьями по результатам 2 прыжков.
#Получить итоговый протокол, содержащий фамилии и результаты, в порядке занятых спортсменами мест по результатам 2 прыжков.

class Athlete:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.total_score = self.calculate_total_score()

    def calculate_total_score(self):
        return sum([sum(jump_scores) for jump_scores in self.scores])


class Competition:
    def __init__(self):
        self.athletes = []

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def calculate_results(self):
        return sorted(self.athletes, key=lambda athlete: athlete.total_score, reverse=True)

    def display_results(self):
        sorted_athletes = self.calculate_results()
        print("Итоговый протокол:")
        for place, athlete in enumerate(sorted_athletes, start=1):
            print(f"{place}. {athlete.name}: {athlete.total_score:.2f}")

if __name__ == "__main__":
    competition = Competition()

    competition.add_athlete(Athlete("Иванов", [[8.5, 9.0, 8.0, 7.5, 9.2], [8.0, 8.5, 9.0, 8.0, 8.5]]))
    competition.add_athlete(Athlete("Петров", [[9.0, 9.5, 9.2, 9.0, 9.1], [9.2, 9.0, 9.1, 9.3, 9.0]]))
    competition.add_athlete(Athlete("Сидоров", [[7.0, 8.0, 7.5, 7.0, 7.5], [8.0, 8.5, 8.0, 8.0, 8.5]]))

    competition.display_results()
