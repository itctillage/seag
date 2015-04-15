# Rubi Yanto - C00163855 - 28/11/2014

from flask import Flask, render_template, url_for, request, redirect, flash, session
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
#APP_STATIC = os.path.join(APP_ROOT, 'static')

app = Flask(__name__)
app.secret_key = '123456'


@app.route('/')
def display_home():
    return render_template("seagoodness.html")

if __name__ == '__main__':
    app.run(debug=True)
