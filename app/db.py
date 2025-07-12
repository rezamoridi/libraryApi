# import sqlalchemy modules to create engin and session manager
from sqlalchemy import create_engine


# import needed modules to use local variables


# import local variables from .env using os.getenv
DB_USER_NAME = "" 
DB_PASSWORD = ""
DB_HOST_NAME = ""
DB_NAME = ""
DB_PORT = ""

# create database url with imported local variables
DATABASE_URL = f"postgresql+psycopg2://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST_NAME}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

# SessionLocal = sessionmaker(autoflush= False, autocommit= False, bind=engine)

# create get_db function to manage sessions
"""def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()"""
