from random import randint, seed
seed(9)
import random
task1 = random.randint(1,15)
print(task1)

#Разделить заданный текст (не более 1000 символов) на строки, содержащие не более 50 символов.
# (Перенос осуществлять на месте пробела.)
# Добавить равномерно пробелы, чтобы каждая строка содер-жала ровно 50 символов.


def justify_text(text, line_width=50):
  
    if len(text) > 1000:
        raise ValueError("Текст не должен превышать 1000 символов.")

    words = text.split()
    lines = []
    current_line = []

    for word in words:
        if sum(len(w) for w in current_line) + len(current_line) + len(word) <= line_width:
            current_line.append(word)
        else:
            lines.append(current_line)
            current_line = [word]

    lines.append(current_line)

    justified_lines = []
    for line in lines:
        if len(line) == 1:
          justified_lines.append(line[0].ljust(line_width))
        else:
            num_spaces = line_width - sum(len(word) for word in line)
            num_gaps = len(line) - 1

            if num_gaps > 0:
                spaces_per_gap = num_spaces // num_gaps
                extra_spaces = num_spaces % num_gaps

                justified_line = ""
                for i in range(len(line) - 1):
                    justified_line += line[i] + " " * (spaces_per_gap + (1 if i < extra_spaces else 0))
                justified_line += line[-1]
                justified_lines.append(justified_line)
            else:
                justified_lines.append("".join(line).ljust(line_width))

    return [line.ljust(line_width) for line in justified_lines]


# Пример использования:
text = "Пример: Разделить заданный текст (не более 1000 символов) на строки, содержащие не более 50 символов. (Перенос осуществлять на месте пробела.) Добавить равномерно пробелы, чтобы каждая строка содер-жала ровно 50 символов."
try:
    justified_text = justify_text(text)

    for line in justified_text:
        print(line)

except ValueError as e:
    print(f"Ошибка: {e}")
