from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from audio.helpers import metadata

app = application = Flask(__name__)
app.config.from_object('audio.config.DevelopmentConfig')

db = SQLAlchemy(app, metadata=metadata)
Migrate(app, db)

import audio.commands

# Business Logic
from audio.controllers.apiv1 import api_v1

app.register_blueprint(api_v1, url_prefix='/apiv1')

from audio import error_handlers
from audio.models.binary import Song, Podcast, Audiobook
