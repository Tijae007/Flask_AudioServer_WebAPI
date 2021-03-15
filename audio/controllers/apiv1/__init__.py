from flask import Blueprint

api_v1 = Blueprint('apiv1', __name__)

from audio.controllers.apiv1 import apiv1_view


@api_v1.before_request
def v1_api_before_request():
    """This will occur after the application's 'before request' has been called."""
    pass


@api_v1.after_request
def v1_api_after_request(response):
    """This will occur after the application's 'after request' has been called."""
    return response
