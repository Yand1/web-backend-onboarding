from flask import Flask
import os
import pathlib

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=str(pathlib.Path(__file__).resolve().parent/'notes.sqlite3'),
)

import notes.demo
import notes.api
import notes.db