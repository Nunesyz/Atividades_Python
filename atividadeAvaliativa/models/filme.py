# Cenário: B Cinema
# Aluno: Lucas Nunes Araújo

from . import db
from .base import ModeloBase


class Filme(ModeloBase):
    __tablename__ = "filme"

    titulo = db.Column(db.String(100), nullable=False)
    duracao = db.Column(db.Integer, nullable=False)

    sessoes = db.relationship("Sessao", backref="filme")