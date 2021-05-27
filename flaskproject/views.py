from flaskproject import app
from flask import (request, render_template, url_for, redirect)


@app.route('/')
@app.route('/home')
def entry_point():
    return render_template(
        'index.html')

