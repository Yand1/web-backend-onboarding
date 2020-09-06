from flask import Flask
import os

app = Flask(__name__)

app.config.from_mapping(
    DATABASE='notes.sqlite',
)

import notes.demo
import notes.api
import notes.db