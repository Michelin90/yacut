from http import HTTPStatus

from flask import jsonify, render_template
from flask.wrappers import Response

from . import app
from .exceptions import InvalidAPIUsage


@app.errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(error: Exception) -> tuple[str, int]:
    return render_template('404.html'), HTTPStatus.NOT_FOUND


@app.errorhandler(HTTPStatus.INTERNAL_SERVER_ERROR)
def internal_error(error: Exception) -> tuple[str, int]:
    return render_template('500.html'), HTTPStatus.INTERNAL_SERVER_ERROR


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: InvalidAPIUsage) -> tuple[Response, int]:
    return jsonify(error.to_dict()), error.status_code
