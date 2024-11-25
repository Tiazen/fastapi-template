import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from  sqlalchemy.orm import declarative_base


SQLALCHEMY_DATABASE_URL = os.environ.get('DB_URL', 'sqlite://') 

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URL,
                        max_overflow=int(os.environ.get('DB_POOL_OVERFLOW', 10)),
                        pool_size=int(os.environ.get('DB_POOL_SIZE', 10)),)

except TypeError:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()