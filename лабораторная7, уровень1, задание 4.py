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
        print("Результаты соревнований по прыжкам в высоту:")
        for index, participant in enumerate(results, start=1):
            print(f"{index}. {participant}")

if __name__ == "__main__":
    competition = Competition()

    alice = Participant("Алиса")
    alice.add_attempt(1.65)
    alice.add_attempt(1.70)
    competition.add_participant(alice)

    bob = Participant("Боб")
    bob.add_attempt(1.75)
    bob.add_attempt(1.80)
    competition.add_participant(bob)

    charlie = Participant("Чарли")
    charlie.add_attempt(1.60)
    charlie.add_attempt(1.65)
    competition.add_participant(charlie)

    competition.display_results()
