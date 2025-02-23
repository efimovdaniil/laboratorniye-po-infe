from random import randint, seed
seed(1009)
import random
task1 = random.randint(1,15)
print(task1)


def read_results(file_path):
    results = {}
    with open(file_path, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            name = data[0]
            attempts = list(map(float, data[1:]))
            results[name] = attempts
    return results


def find_best_results(results):
    best_results = {}
    for name, attempts in results.items():
        best_results[name] = max(attempts)
    return best_results


def write_final_protocol(best_results, output_file):
    sorted_results = sorted(best_results.items(), key=lambda item: item[1], reverse=True)

    with open(output_file, 'w') as file:
        file.write("Итоговый протокол соревнований по прыжкам в длину:\n")
        file.write("Фамилия, Лучший результат\n")
        for name, best in sorted_results:
            file.write(f"{name}, {best:.2f}\n")


if __name__ == "__main__":
    input_file = 'long_jump_results.txt'
    output_file = 'final_protocol.txt'
    results = read_results(input_file)

    best_results = find_best_results(results)

    write_final_protocol(best_results, output_file)

    print(f"Итоговый протокол записан в файл '{output_file}'.")
