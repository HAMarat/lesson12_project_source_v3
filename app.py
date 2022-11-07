from flask import Flask, request, render_template, send_from_directory
from functions import find_posts
from loader.loader import loader
from main.main import main


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.register_blueprint(main, url_prefix='')
app.register_blueprint(loader, url_prefix='')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html', title='Страница не найдена'), 404


@app.route('/search/', methods=['GET'])
def search_posts():
    s = request.args['s']
    find_posts_dict = find_posts(s)
    if find_posts_dict:
        return render_template('post_list.html', find_posts_dict=find_posts_dict, s=s)
    return "Не найдено"


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
