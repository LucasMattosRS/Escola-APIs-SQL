from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estudante(Base):
    __tablename__ = 'estudantes'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    email = Column(String)
    perfil = relationship("Perfil",
        back_populates="estudante",
        uselist=False,
        cascade="all, delete-orphan"
    )
    matriculas = relationship(
        "Matricula", 
        back_populates="estudante",
        cascade="all, delete-orphan"
    )
    professor_id = Column(Integer, ForeignKey("professores.id"))
    professor = relationship(
        "Professor", 
        back_populates="estudantes"
    )


class Perfil(Base):
    __tablename__ = 'perfis'
    id = Column(Integer, primary_key=True, index=True)
    idade = Column(Integer)
    endereco = Column(String)
    estudante_id = Column(
        Integer,
        ForeignKey("estudantes.id"),
        unique=True
    )
    estudante = relationship(
        "Estudante",
        back_populates='perfil'
    )

class Disciplina(Base):
    __tablename__ = "disciplinas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    matriculas = relationship(
        "Matricula",
        back_populates='disciplina',
        cascade="all, delete-orphan"
    )

class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(Integer, primary_key=True, index=True)
    estudante_id = Column(Integer, ForeignKey("estudantes.id"))
    estudante = relationship(
        "Estudante",
        back_populates='matriculas'
    )
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    disciplina = relationship(
        "Disciplina",
        back_populates='matriculas'
    )

class Professor(Base):
    __tablename__ = "professores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    estudantes = relationship(
        "Estudante", 
        back_populates="professor",
        cascade="all, delete-orphan"
    )
