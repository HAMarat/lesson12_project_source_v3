import json


def load_json_posts() -> list[dict]:
    """
    Загружаем данные из json файла
    """
    with open('posts.json', 'r', encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def find_posts(text_search):
    find_posts_dict = []
    for post in load_json_posts():
        if text_search in post["content"]:
            find_posts_dict.append(post)
    return find_posts_dict

