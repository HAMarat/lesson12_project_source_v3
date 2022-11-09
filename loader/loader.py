import logging

from flask import Blueprint, render_template, request
from functions import append_json_data
loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static')

UPLOAD_FOLDER = "uploads/images"


@loader.route('/post')
def load_post():
    """
    Представление для отображения страницы загрузки поста
    """
    return render_template('post_form.html')


@loader.route('/post', methods=['POST'])
def post_uploaded():
    """
    Представление для обработки формы загрузки поста и отображения страницы загруженного файла
    """
    # получаем объект из формы
    post_picture = request.files.get('picture')

    if not post_picture:
        logging.error("Файл не загружен")
        return "Файл не загружен"

    # сохраняем название объекта
    file_name = post_picture.filename

    # создаем путь для сохранения объекта с оригинальным названием
    path_load = f'{UPLOAD_FOLDER}/{file_name}'

    # сохраняем объект по ранее полученному пути
    post_picture.save(f'./{path_load}')

    # сохраняем текст полученный из формы 'content'
    post_text = request.form.get('content')

    # вызываем функцию для сохранения данных поста в json файл
    append_json_data(path_load, post_text)

    return render_template('post_uploaded.html', post_text=post_text, path_load=path_load)
