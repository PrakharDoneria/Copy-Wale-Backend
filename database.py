from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your PostgreSQL database details
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"  # Update with your details

# Create the database engine and session maker
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()
