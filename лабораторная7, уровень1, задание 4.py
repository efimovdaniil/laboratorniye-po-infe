from random import randint, seed
seed(9)
x1 = randint(1,5)
x2 = randint(1,9)
x3 = randint(1,6)
print(x1,x2,x3)


#Результаты соревнований по прыжкам в высоту определяются по лучшей из двух попыток. Вывести список участников в порядке занятых мест.

class Participant:
    def __init__(self, name):
        self.name = name
        self.attempts = []

    def add_attempt(self, height):
        self.attempts.append(height)

    def best_attempt(self):
        return max(self.attempts) if self.attempts else 0

    def __str__(self):
        return f"{self.name}: {self.best_attempt()} m"


class Competition:
    def __init__(self):
        self.participants = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def get_results(self):
        return sorted(self.participants, key=lambda p: p.best_attempt(), reverse=True)

    def display_results(self):
        results = self.get_results()
        print("\nРезультаты соревнований по прыжкам в высоту:")
        for index, participant in enumerate(results, start=1):
            print(f"{index}. {participant}")


def main():
    competition = Competition()

    num_participants = int(input("Введите количество участников: "))

    for _ in range(num_participants):
        name = input("Введите имя участника: ")
        participant = Participant(name)

        num_attempts = int(input(f"Введите количество попыток для {name}: "))
        for _ in range(num_attempts):
            height = float(input("Введите высоту прыжка (в метрах): "))
            participant.add_attempt(height)

        competition.add_participant(participant)


    competition.display_results()


if __name__ == "__main__":
    main()
