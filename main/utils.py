import json
import logging
from json import JSONDecodeError

POST_PATH = 'posts.json'


def load_json_posts() -> list[dict] | None:
    """
    Загружаем данные из json файла
    """
    try:
        with open(POST_PATH, 'r', encoding='utf-8') as file:
            posts = json.load(file)
    except FileNotFoundError:
        with open(POST_PATH, 'w', encoding='utf-8') as new_file:
            posts = new_file
            logging.info(f"Файл {POST_PATH}, не найден, создан новый")
    except JSONDecodeError:
        with open(POST_PATH, 'w', encoding='utf-8') as new_file:
            posts = new_file
            logging.info(f"Файл {POST_PATH}, не удалось преобразовать. Файл перезаписан")
    return posts
