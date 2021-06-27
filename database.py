import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://%s:%s@%s:%s/%s" % (os.environ["BBDD_USER"], \
                                                           os.environ["BBDD_PASSWORD"], \
                                                           os.environ["BBDD_HOST"], \
                                                           os.environ["BBDD_PORT"], \
                                                           os.environ["BBDD_DATABASE"])

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
