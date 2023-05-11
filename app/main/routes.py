# import os
# from datetime import datetime
from flask import render_template #, flash, redirect

# from app import app
# from app import db
from app.main import bp
# import app.main.forms as forms
# from flask_login import current_user, login_required


# @app.before_request
# def before_request():
#     if current_user.is_authenticated:
#         current_user.last_seen = datetime.utcnow()
#         db.session.commit()


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/home', methods=['GET', 'POST'])
def homepage():
    return render_template('main/main.html')


# @bp.route('/projects')
# @login_required
# def projects():
#     return render_template('main/projects.html')


# @bp.route('/writings')
# def writings():
#     return render_template('main/writings.html')


# @bp.route('/resume', methods=['GET', 'POST'])
# def resume():
#     form = forms.ResumeForm()
#     if form.validate_on_submit():
#         print("FORM VALIDATED...")
#         flash('Resume requested for {}'.format(
#             form.email_address.data))
#         return redirect(os.getenviron('RESUME_PATH'))
#
#     return render_template('main/resume.html', title='Download Resume', form=form)


# # TESTING
# @bp.route('/spin')
# @login_required
# def spin():
#     return render_template('testing/spinning_word.html')