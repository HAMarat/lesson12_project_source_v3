from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.main import main

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main, url_prefix='')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html', title='Страница не найдена'), 404


@app.route('/search/?s=<ключ поиска>')



@app.route("/")
def page_index():
    return "Первая страница"


@app.route("/list")
def page_tag():
    pass


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    pass


@app.route("/post", methods=["POST"])
def page_post_upload():
    pass


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True, host='127.0.0.1', port=3000)
