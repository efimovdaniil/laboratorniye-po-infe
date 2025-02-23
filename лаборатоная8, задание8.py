from random import randint, seed
seed(9)
import random
task1 = random.randint(1,15)
print(task1)

def format_text(text, line_length=50):
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + (1 if current_line else 0) <= line_length:
            if current_line:
                current_line += " "
            current_line += word
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    formatted_lines = []
    for line in lines:
        if len(line) < line_length:
            words_in_line = line.split()
            total_spaces = line_length - len(line)
            if len(words_in_line) > 1:
                spaces_between_words = total_spaces // (len(words_in_line) - 1)
                extra_spaces = total_spaces % (len(words_in_line) - 1)

                for i in range(len(words_in_line) - 1):
                    formatted_lines.append(words_in_line[i])
                    formatted_lines.append(" " * (spaces_between_words + (1 if i < extra_spaces else 0)))
                formatted_lines.append(words_in_line[-1])  # Последнее слово без пробела
            else:
                formatted_lines.append(line + " " * (line_length - len(line)))
        else:
            formatted_lines.append(line)

    return ''.join(formatted_lines)


# Пример использования
if __name__ == "__main__":
    text = (
        "Это пример текста, который мы будем использовать для "
        "разделения на строки, содержащие не более пятидесяти символов. "
        "Каждая строка будет дополнена пробелами, чтобы выровнять её "
        "по ширине. Давайте посмотрим, как это будет выглядеть."
    )

    formatted_text = format_text(text)
    print(formatted_text)
