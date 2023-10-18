from flask import jsonify, render_template
from flask.wrappers import Response

from . import app
from .exceptions import InvalidAPIUsage


@app.errorhandler(404)
def page_not_found(error: Exception) -> tuple[str, int]:
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error: Exception) -> tuple[str, int]:
    return render_template('500.html'), 500


@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error: InvalidAPIUsage) -> tuple[Response, int]:
    return jsonify(error.to_dict()), error.status_code
