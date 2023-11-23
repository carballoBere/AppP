from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('lenguajes', __name__,url_prefix="/lenguaje/")

@bp.route('/')
def index():
    db = get_db()
    lenguajes = db.execute(
        """SELECT l.name AS lenguaje FROM language l 
           ORDER BY lenguaje ASC"""
    ).fetchall()
    return render_template('lenguaje/index.html', lenguajes=lenguajes)


