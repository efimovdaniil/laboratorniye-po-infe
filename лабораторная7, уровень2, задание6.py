#Протокол соревнований по прыжкам в воду содержит список фамилий спортсменов и баллы, выставленные 5 судьями по результатам 2 прыжков.
#Получить итоговый протокол, содержащий фамилии и результаты, в порядке занятых спортсменами мест по результатам 2 прыжков.

class Athlete:
    def __init__(self, name):
        self.name = name
        self.scores = []

    def add_scores(self, jump_scores):
        self.scores.append(jump_scores)

    def total_score(self):
        return sum(self.scores)

    def __str__(self):
        return f"{self.name}: {self.total_score()}"


class Competition:
    def __init__(self):
        self.athletes = []

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def get_results(self):
        return sorted(self.athletes, key=lambda a: a.total_score(), reverse=True)

    def display_results(self):
        results = self.get_results()
        print("\nИтоговый протокол соревнований по прыжкам в воду:")
        for index, athlete in enumerate(results, start=1):
            print(f"{index}. {athlete}")


def main():
    competition = Competition()

    num_athletes = int(input("Введите количество спортсменов: "))

    for _ in range(num_athletes):
        name = input("Введите фамилию спортсмена: ")
        athlete = Athlete(name)

        for jump in range(1, 3):
            scores = []
            print(f"\nВведите баллы за прыжок {jump} (5 судей):")
            for judge in range(1, 6):  # 5 судей
                score = float(input(f"Баллы от судьи {judge}: "))
                scores.append(score)

            scores.remove(max(scores))
            scores.remove(min(scores))
            athlete.add_scores(sum(scores))

        competition.add_athlete(athlete)
    competition.display_results()


if __name__ == "__main__":
    main()
