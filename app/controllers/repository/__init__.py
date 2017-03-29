from flask import Blueprint
repository = Blueprint('repository', __name__)

from . import views