from flask import(
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint ('pelis',__name__)
@bp.route('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT l.name as lenguage, f.title as titulo
            from language l JOIN film f ON l.language_id = f.language_id
            ORDER BY name ASC"""
    ).fetchall()
    return render_template('pelis/index.html',pelis = pelis)