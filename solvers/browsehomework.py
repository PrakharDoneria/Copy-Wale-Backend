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

# Get nearby homework (solvers browsing tasks)
@router.get("/nearby")
def browse_homework(latitude: float, longitude: float, radius_km: float = 5, db: Session = Depends(get_db)):
    # Use haversine formula or similar to filter homework by distance if needed
    homeworks = crud.get_homeworks_within_radius(db, latitude, longitude, radius_km)
    return homeworks
