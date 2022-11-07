from flask import Blueprint, render_template

loader = Blueprint('loader', __name__, template_folder='templates', static_folder='static')


@loader.route('/post')
def load_post():
    return render_template('post_form.html')
