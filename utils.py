from main.utils import load_json_posts


def find_posts(text_search: str) -> list[dict]:
    """
    Ищем посты в которых содержится искомый ключ поиска
    """
    find_posts_dict = []
    for post in load_json_posts():
        if text_search in post["content"]:
            find_posts_dict.append(post)
    return find_posts_dict
