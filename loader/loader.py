from flask import Blueprint, render_template, request
from functions import append_json_data
loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static')


@loader.route('/post')
def load_post():
    return render_template('post_form.html')


@loader.route('/post_uploaded', methods=['POST'])
def post_uploaded():
    post_picture = request.files.get('picture')
    file_name = post_picture.filename
    path_load = f'./uploads/images/{file_name}'
    post_picture.save(path_load)

    post_text = request.form.get('content')

    append_json_data(path_load, post_text)

    return render_template('post_uploaded.html', post_text=post_text, path_load=path_load)
