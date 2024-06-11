from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from marshmallow import Schema, fields

from database.database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    password = Column(String)

    def __init__(self, email, password):
        self.email = email
        self.password = generate_password_hash(password)

    def password_hash(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Venda(Base):
    __tablename__ = 'vendas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome_cliente = Column(String)
    produto = Column(String)
    valor = Column(Float)
    data_venda = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="vendas")

    def __init__(self, nome_cliente, produto, valor, data_venda, user_id):
        self.nome_cliente = nome_cliente
        self.produto = produto
        self.valor = valor
        self.data_venda = data_venda
        self.user_id = user_id


# Defina o relacionamento inverso no modelo User
User.vendas = relationship("Venda", back_populates="user")


class VendaSchema(Schema):
    id = fields.Integer()
    nome_cliente = fields.String()
    produto = fields.String()
    valor = fields.Float()
    data_venda = fields.DateTime()
    user_id = fields.Integer()
