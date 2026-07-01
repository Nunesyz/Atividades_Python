from . import db
from .base import ModeloBase


class Sessao(ModeloBase):
    __tablename__ = "sessao"

    horario = db.Column(db.DateTime, nullable=False)
    filme_id = db.Column(db.Integer, db.ForeignKey("filme.id"), nullable=False)
    sala_id = db.Column(db.Integer, db.ForeignKey("sala.id"), nullable=False)