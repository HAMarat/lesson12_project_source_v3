import logging
from flask import Flask, request, render_template, send_from_directory
from utils import find_posts
from loader.loader import loader
from main.main import main


app = Flask(__name__)

app.register_blueprint(main, url_prefix='')
app.register_blueprint(loader, url_prefix='')

logging.basicConfig(filename="logs/basic.log", level=logging.INFO)


@app.errorhandler(404)
def page_not_found(error):
    """
    Представление для обработки ошибки не найденной страницы
    """
    return render_template('404.html', title='Страница не найдена'), 404


@app.route('/search/', methods=['GET'])
def search_posts():
    """
    Представление для отображения найденных постов
    """
    search_text = request.args['s']
    find_posts_dict = find_posts(search_text)
    logging.info(f"Выполнен поиск по запросу {search_text}")
    return render_template('post_list.html', find_posts_dict=find_posts_dict, search_text=search_text)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True, host='127.0.0.1', port=3000)
