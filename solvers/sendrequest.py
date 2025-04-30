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

# Send a request to solve homework
@router.post("/sendrequest")
def send_request(homework_id: int, solver_nickname: str, message: str, contact_info: str, db: Session = Depends(get_db)):
    request = crud.create_request(db, homework_id, solver_nickname, message, contact_info)
    return request
