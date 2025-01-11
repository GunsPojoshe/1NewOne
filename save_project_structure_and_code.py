# save_project_structure_and_code.py
import os

def save_project_structure_and_code(root_dir, output_file):
    """
    Сохраняет структуру проекта и содержимое всех файлов в текстовый файл.

    :param root_dir: Корневая директория проекта.
    :param output_file: Имя файла для сохранения структуры и кода.
    """
    with open(output_file, "w", encoding="utf-8") as outfile:
        # Рекурсивно обходим все папки и файлы
        for root, dirs, files in os.walk(root_dir):
            # Игнорируем папку venv и другие ненужные папки
            if "venv" in root or "__pycache__" in root:
                continue

            # Записываем текущую папку
            outfile.write(f"cd {root}\n")
            outfile.write("(Папка)\n\n")  # Добавляем пометку "Папка"

            # Записываем файлы в текущей папке
            for file in files:
                file_path = os.path.join(root, file)
                outfile.write(f"cd {file_path}\n")

                # Записываем содержимое файла (если это текстовый файл)
                if file.endswith((".py", ".txt", ".md", ".html", ".env")):
                    outfile.write("\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as infile:
                            content = infile.read()
                            if content.strip():  # Проверяем, не пустой ли файл
                                outfile.write(content)
                            else:
                                outfile.write("В этом файле нет кода.\n")
                    except UnicodeDecodeError:
                        outfile.write("(Ошибка чтения: неверная кодировка)\n")
                    outfile.write("\n\n")

# Путь к корневой директории проекта
root_dir = os.path.dirname(os.path.abspath(__file__))

# Имя файла для сохранения структуры и кода
output_file = "project_structure_and_code.txt"

# Сохраняем структуру проекта и код
save_project_structure_and_code(root_dir, output_file)
print(f"Структура проекта и код успешно сохранены в {output_file}")