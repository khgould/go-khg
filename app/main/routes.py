from flask import render_template
from app.main import bp


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/home', methods=['GET', 'POST'])
def homepage():
    return render_template('main/main.html')


@bp.route('/photos')
def photos():
    return render_template('main/photos.html')


@bp.route('/notes')
def notes():
    return render_template('main/notes.html')

# @bp.route('/recs')
# def recs():
#     return render_template('main/recommendations.html')

@bp.route('/meet')
def meet():
    return render_template('main/meet.html')