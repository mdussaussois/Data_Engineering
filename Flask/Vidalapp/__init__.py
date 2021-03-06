from flask import Flask
from .views import app

from . import utils

@app.cli.command()
def init_db():
    utils.init_db()
