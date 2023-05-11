import logging
from flask import render_template, flash, redirect, url_for, request
from app.contact import bp
import app.contact.forms as forms
from flask_mail import Message
from app import mail

@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = forms.ContactMe()
    if form.validate_on_submit():
        flash('Note sent to Kevin from {}'.format(
            form.name.data))
        if request.method == 'POST':
            recipient = request.form['recipient']
            msg = Message('Message submitted from your website: go-KHG', recipients=[recipient])
            msg.body = form.data.message
            mail.send(msg)
            logging.info('Message sent...')
            flash(f'your message was sent to kevin')
        return redirect(url_for('main.home'))
    return render_template('email/contact_form.html', title='Sign In', form=form)