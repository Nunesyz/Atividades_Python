from . import db
from .base import ModeloBase


class Sala(ModeloBase):
    __tablename__ = "sala"

    nome = db.Column(db.String(50), nullable=False)
    capacidade = db.Column(db.Integer, nullable=False)

    sessoes = db.relationship("Sessao", backref="sala")
