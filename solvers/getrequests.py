from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
import crud

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all requests sent by the solver
@router.get("/myrequests/{solver_nickname}")
def get_requests(solver_nickname: str, db: Session = Depends(get_db)):
    return crud.get_requests_by_solver(db, solver_nickname)
