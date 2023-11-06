from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_URL = 'sqlite:///database.db'
engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

from database import models


# генератор подключений
def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()
