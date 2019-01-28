# -*- coding: utf-8 -*-

from flask import render_template, flash, redirect, url_for, request, g, current_app
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
from datetime import datetime
from app import db
from app.main import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, \
                    ResetPasswordForm
from app.main.forms import EditProfileForm
from app.models import User
from app.auth.email import send_password_reset_email
from flask_babel import _, get_locale

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    user = {'username': 'Yoh'}
    app_name = current_app.config['APP_NAME']
    return render_template('index.html', title=_('Home'), app_name=app_name)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


@bp.route('/edit_profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title=_('Edit Profile'), form=form)
