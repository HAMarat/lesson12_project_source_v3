from flask import Blueprint, render_template, request
from functions import append_json_data
loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static')

UPLOAD_FOLDER = "uploads/images"
ALLOWED_EXTENSIONS = ['jpg', 'jpeg', 'png']


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
    post_picture = request.files.get('picture')
    file_name = post_picture.filename
    path_load = f'{UPLOAD_FOLDER}/{file_name}'
    post_picture.save(f'./{path_load}')

    post_text = request.form.get('content')

    append_json_data(path_load, post_text)

    return render_template('post_uploaded.html', post_text=post_text, path_load=path_load)
