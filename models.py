from sqlalchemy import Column, Integer, String, Text, Numeric
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    email = Column(String)
    telefone = Column(String)
    cidade = Column(String)
    valor = Column(Numeric)
    experiencia = Column(Text, nullable=True, default="Sem experiência")