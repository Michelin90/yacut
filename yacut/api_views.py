import re

from flask import jsonify, request
from flask.wrappers import Response

from . import app, db
from .exceptions import InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_url(short_id: str) -> tuple[Response, int]:
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage('Указанный id не найден', 404)
    return jsonify({'url': url_map.to_dict().get('original')}), 200


@app.route('/api/id/', methods=['POST'])
def create_url_map() -> tuple[Response, int]:
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if not data.get('url') or data.get('url') == '':
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    custom_id = data.get('custom_id')
    url_map = URLMap()
    if not custom_id or custom_id == '':
        custom_id = url_map.get_unique_short_id()
        data['custom_id'] = custom_id
    pattern = r'^[A-Za-z0-9]{1,16}$'
    if not re.match(pattern, custom_id):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки'
        )
    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(
            'Предложенный вариант короткой ссылки уже существует.'
        )
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    to_dict = url_map.to_dict()
    return jsonify({
        'url': to_dict.get('original'),
        'short_link': 'http://localhost/' + to_dict.get('short')
    }), 201