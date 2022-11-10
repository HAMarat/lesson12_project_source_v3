import json
from main.utils import load_json_posts, POST_PATH


def is_file_extension_allowed(filename: str, extensions: list) -> bool:
    """
    Добавляем данные нового поста в json файл
    """
    extension = filename.split('.')[-1].lower()
    if extension in extensions:
        return True
    return False


def append_json_data(path: str, text: str) -> None:
    """
    Добавляем данные нового поста в json файл
    """
    json_data = load_json_posts()
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        post_dict = {'pic': path, 'content': text}
        json_data.append(post_dict)
        json.dump(json_data, file, ensure_ascii=False, indent=4)
