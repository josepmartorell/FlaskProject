"""
Routes and views for the flask application.
"""
from datetime import datetime
from flaskproject import app
from flask import (request, render_template, url_for, redirect)
from flaskproject.models import Note
from flaskproject.forms import NoteForm
from flaskproject import db


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    notes = Note.query.filter_by(is_deleted=False).all()
    return render_template(
        'index.html',
        title='Note List',
        year=datetime.now().year,
        notes=notes,
    )


@app.route('/new-note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        form = NoteForm(request.form)
        if form.validate():
            note = Note(form.subject.data, form.detail.data)
            db.session.add(note)
            db.session.commit()
            return redirect(url_for('home'))
    else:
        form = NoteForm()
        return render_template(
            'create_note.html',
            title='Create New Note',
            year=datetime.now().year,
            form=form
        )


