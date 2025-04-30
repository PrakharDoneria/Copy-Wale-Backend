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

# Get homework posts by nickname (for students to view their posts)
@router.get("/{nickname}")
def get_homework_by_nickname(nickname: str, db: Session = Depends(get_db)):
    return crud.get_homeworks_by_nickname(db, nickname)
