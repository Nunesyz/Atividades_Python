from datetime import datetime

from flask import Blueprint, redirect, render_template, request, url_for

from models import Filme, Sala, Sessao, db

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")


@cinema_bp.route("/")
def index():
    sessoes = Sessao.query.all()
    return render_template("cinema/index.html", sessoes=sessoes)


@cinema_bp.route("/nova", methods=["GET", "POST"])
def nova_sessao():
    filmes = Filme.query.all()
    salas = Sala.query.all()
    if request.method == "POST":
        sessao = Sessao(
            horario=datetime.strptime(request.form["horario"], "%Y-%m-%dT%H:%M"),
            filme_id=request.form["filme_id"],
            sala_id=request.form["sala_id"],
        )
        db.session.add(sessao)
        db.session.commit()
        return redirect(url_for("cinema.index"))
    return render_template("cinema/nova_sessao.html", filmes=filmes, salas=salas)