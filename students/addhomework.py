from fastapi import APIRouter, Depends, HTTPException
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

# Post homework (for students)
@router.post("/")
def post_homework(title: str, description: str, subject: str, budget: float, latitude: float, longitude: float, contact_info: str, nickname: str, db: Session = Depends(get_db)):
    return crud.create_homework(db, title, description, subject, budget, latitude, longitude, contact_info, nickname)
