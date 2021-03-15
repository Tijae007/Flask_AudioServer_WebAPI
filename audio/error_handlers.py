from flask import jsonify
import sqlalchemy

from audio import app


@app.errorhandler(400)
def error400(error):
    """Handles abort(400) calls in code.
    """
    try:
        response = jsonify({'code': 400, "description": error.description})
    except (Exception,):
        response = jsonify({'code': 400, "description": error._message()})

    response.status_code = 400
    return response


@app.errorhandler(500)
def error500(error):
    """
    Handles abort(500) calls in code.
    """
    print(dir(error))
    try:
        response = jsonify({'code': 500, "description": error.description})
    except (Exception,):
        response = jsonify({'code': 500, "description": error._message()})

    response.status_code = 500
    return response


@app.errorhandler(Exception)
def unhandled_exception(error):
    print(dir(error))
    try:
        response = jsonify({'code': 500, "description": error.description})
    except (Exception,):
        response = jsonify({'code': 500, "description": error._message()})

    response.status_code = 500
    return response
