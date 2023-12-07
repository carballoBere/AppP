from flask import(
    Blueprint,flash,g,redirect,render_template,request,url_for
)
from werkzeug.exceptions import abort

from peliculas.db import get_db

bp = Blueprint ('pelis',__name__, url_prefix="/pelis")
@bp.route('/')
def index():
    db = get_db()
    pelis = db.execute(
        """SELECT title as titulo, film_id
            FROM film 
            ORDER BY titulo ASC"""
    ).fetchall()
    return render_template('pelis/index.html',pelis = pelis)

@bp.route('/<int:id>')
def detalle(id):
    peli = get_db().execute(
        """SELECT l.name as lenguaje, f.title as titulo
            FROM language l JOIN film f ON l.language_id = f.language_id
            WHERE f.film_id = ?""", (id,)
            ).fetchone()
    actores = get_db().execute(
        """SELECT a.first_name, a.last_Name, a.actor_id FROM film f
        JOIN film_actor fa ON f.film_id = fa.film_id
        JOIN actor a ON fa.actor_id = a.actor_id
        WHERE f.film_id = ?""", (id,)
            ).fetchall()
    return render_template('pelis/detalle.html',peli=peli, actores=actores )