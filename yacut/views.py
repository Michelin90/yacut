import re

from flask import flash, redirect, render_template, url_for
from werkzeug.wrappers.response import Response

from . import app, db
from .forms import UrlForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def add_url_map() -> str:
    form = UrlForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        pattern = r'^[A-Za-z0-9]{1,16}$'
        if custom_id and not re.match(pattern, custom_id):
            flash(
                'Указано недопустимое имя для короткой ссылки.',
                'too_long'
            )
            return render_template('index.html', form=form)
        if URLMap.query.filter_by(short=custom_id).first():
            flash(
                'Предложенный вариант короткой ссылки уже существует.',
                'non-unique'
            )
            return render_template('index.html', form=form)
        url_map = URLMap(
            original=form.original_link.data,
            short=(
                form.custom_id.data if form.custom_id.data
                else URLMap.get_unique_short_id()
            )
        )
        db.session.add(url_map)
        db.session.commit()
        flash(url_for(
            'follow_url_map', short=url_map.short, _external=True
            ), 'link'
        )
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def follow_url_map(short: str) -> Response:
    url_map = URLMap.query.filter_by(short=short).first_or_404()
    return redirect(url_map.original)
