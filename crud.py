from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float

# Homework model (for students)
class Homework:
    __tablename__ = 'homeworks'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    subject = Column(String)
    budget = Column(Float)
    latitude = Column(Float)
    longitude = Column(Float)
    contact_info = Column(String)
    nickname = Column(String)

# Request model (for solvers)
class Request:
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, index=True)
    homework_id = Column(Integer)
    solver_nickname = Column(String)
    message = Column(String)
    contact_info = Column(String)
    status = Column(String, default="pending")  # 'pending', 'accepted', 'rejected'

# Create a homework post (student side)
def create_homework(db: Session, title: str, description: str, subject: str, budget: float, latitude: float, longitude: float, contact_info: str, nickname: str):
    db_homework = Homework(
        title=title,
        description=description,
        subject=subject,
        budget=budget,
        latitude=latitude,
        longitude=longitude,
        contact_info=contact_info,
        nickname=nickname,
    )
    db.add(db_homework)
    db.commit()
    db.refresh(db_homework)
    return db_homework

# Get all homework posts by nickname (student side)
def get_homeworks_by_nickname(db: Session, nickname: str):
    return db.query(Homework).filter(Homework.nickname == nickname).all()

# Delete a homework post (student side)
def delete_homework(db: Session, homework_id: int):
    homework = db.query(Homework).filter(Homework.id == homework_id).first()
    if homework:
        db.delete(homework)
        db.commit()
    return homework

# Create a request to solve a homework (solver side)
def create_request(db: Session, homework_id: int, solver_nickname: str, message: str, contact_info: str):
    db_request = Request(
        homework_id=homework_id,
        solver_nickname=solver_nickname,
        message=message,
        contact_info=contact_info,
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request

# Get all requests sent by a solver (solver side)
def get_requests_by_solver(db: Session, solver_nickname: str):
    return db.query(Request).filter(Request.solver_nickname == solver_nickname).all()

# Get homework posts within a given radius (simplified version, not using haversine formula here)
def get_homeworks_within_radius(db: Session, latitude: float, longitude: float, radius_km: float):
    return db.query(Homework).all()  # For now, returns all homeworks (you can implement radius filtering logic here)
