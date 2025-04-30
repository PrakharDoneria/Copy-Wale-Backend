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

# Delete a homework post
@router.delete("/{homework_id}")
def delete_homework(homework_id: int, db: Session = Depends(get_db)):
    deleted_homework = crud.delete_homework(db, homework_id)
    if not deleted_homework:
        raise HTTPException(status_code=404, detail="Homework not found")
    return {"msg": "Homework deleted successfully"}
