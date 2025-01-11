# Файл: create_gist.py
import os
import requests
import logging
from typing import Dict, Any
from dotenv import load_dotenv

# Загружаем переменные из файла Keys.env
load_dotenv("Keys.env")

# Получаем токен GitHub из переменных окружения
GITHUB_TOKEN = os.getenv("GITHUB_GISTS_KEY")
print(f"Токен: {GITHUB_TOKEN}")  # Отладочный вывод# Отладочный вывод

print("Загруженные переменные:")
print(f"GITHUB_GISTS_KEY: {GITHUB_TOKEN}")

# Путь к директории с файлами
PROJECT_DIR = r"C:/Games/1NewOne"  # Указанный вами путь

# Настройка логирования
logging.basicConfig(filename='create_gist.log', level=logging.ERROR)

def read_file(file_path: str) -> str:
    """
    Читает содержимое файла.
    
    :param file_path: Путь к файлу.
    :return: Содержимое файла.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return ""

def create_gist(files: Dict[str, Dict[str, str]], description: str = "Automated Gist", public: bool = True) -> str:
    """
    Создает Gist на GitHub.
    
    :param files: Словарь с файлами для загрузки.
    :param description: Описание Gist.
    :param public: Если True, Gist будет публичным.
    :return: Ссылка на созданный Gist.
    """
    url = "https://api.github.com/gists"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json",
    }
    data = {
        "description": description,
        "public": public,
        "files": files,
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Ответ от API: {response.status_code}, {response.text}")  # Отладочный вывод
        if response.status_code == 201:
            return response.json()["html_url"]
        else:
            raise Exception(f"Ошибка при создании Gist: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Ошибка при отправке запроса к API GitHub: {e}")
        raise

def collect_files(directory: str) -> Dict[str, Dict[str, str]]:
    """
    Собирает файлы из директории.
    
    :param directory: Путь к директории.
    :return: Словарь с файлами для загрузки в Gist.
    """
    files = {}
    ignore_dirs = {"venv", ".git", "__pycache__"}
    for root, dirs, filenames in os.walk(directory):
        # Игнорируем ненужные папки
        dirs[:] = [d for d in dirs if d not in ignore_dirs]
        
        for filename in filenames:
            if filename.endswith((".py", ".txt", ".md", ".html", ".env")):
                file_path = os.path.join(root, filename)
                relative_path = os.path.relpath(file_path, directory)
                content = read_file(file_path)
                if content:
                    files[relative_path] = {"content": content}
                    print(f"Добавлен файл: {relative_path}")  # Отладочный вывод
    return files

def main():
    """
    Основная функция для создания Gist.
    """
    try:
        # Собираем файлы
        files = collect_files(PROJECT_DIR)
        if not files:
            print("Файлы для загрузки не найдены.")
            return
        
        # Создаем Gist
        gist_url = create_gist(files, description="1NewOne Project Files")
        print(f"Gist успешно создан: {gist_url}")
    except Exception as e:
        logging.error(f"Ошибка при создании Gist: {e}")
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()