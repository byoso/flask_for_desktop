#! /usr/bin/env python3
# -*- coding : utf-8 -*-

from flask import request, render_template, redirect, flash, url_for
from werkzeug.urls import url_parse

from flaskapp.app import app

@app.route("/")
def index():
    return render_template("index.html")
