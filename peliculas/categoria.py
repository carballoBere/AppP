from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint('categorias', __name__,url_prefix="/categoria/")

@bp.route('/')
def index():
    db = get_db()
    categorias = db.execute(
        """SELECT name AS categoria
            FROM category
            ORDER BY categoria ASC"""
    ).fetchall()
    return render_template('categoria/index.html', categorias=categorias)
