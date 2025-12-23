from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import modelos, schemas
from database import engine, SessionLocal
from typing import List
from sqlalchemy.orm import joinedload

modelos.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/estudantes/', response_model=schemas.Estudante)
def criar_estudante(
        estudante: schemas.EstudanteCreate,
        db: Session = Depends(get_db)
    ):
    db_estudante = modelos.Estudante(
        nome = estudante.nome,
        perfil = modelos.Perfil(**estudante.perfil.dict())
    )
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante

@app.get('/estudantes/', response_model=List[schemas.Estudante])
def listar_estudantes(db: Session = Depends(get_db)):
    estudantes = db.query(modelos.Estudante).options(
        joinedload(modelos.Estudante.perfil)
    ).all()
    return estudantes

# DISCIPLINAS

@app.post('/disciplinas/', response_model=schemas.Disciplina)
def criar_disciplina(
        disciplina: schemas.DisciplinaCreate,
        db: Session = Depends(get_db)
    ):
    db_disciplina = modelos.Disciplina(**disciplina.dict())
    db.add(db_disciplina)
    db.commit()
    db.refresh(db_disciplina)
    return db_disciplina

@app.get('/disciplinas/', response_model=List[schemas.Disciplina])
def listar_disciplinas(db: Session = Depends(get_db)):
    return db.query(modelos.Disciplina).all()


# PROFESSORES

@app.post('/professores/', response_model=schemas.Professor)
def criar_professor(
        professor: schemas.ProfessorCreate,
        db: Session = Depends(get_db)
    ):
    db_professor = modelos.Professor(**professor.dict())
    db.add(db_professor)
    db.commit()
    db.refresh(db_professor)
    return db_professor

@app.get('/professores/', response_model=List[schemas.Professor])
def listar_professores(db: Session = Depends(get_db)):
    return db.query(modelos.Professor).all()


# MATRÍCULAS

@app.post('/matriculas/', response_model=schemas.Matricula)
def criar_matricula(
        matricula: schemas.MatriculaCreate,
        db: Session = Depends(get_db)
    ):
    db_matricula = modelos.Matricula(**matricula.dict())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get('/matriculas/', response_model=List[schemas.Matricula])
def listar_matriculas(db: Session = Depends(get_db)):
    return db.query(modelos.Matricula).all()
