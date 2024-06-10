from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config.config import Config

Base = declarative_base()

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI) # Passa a url definida em config/config.ini
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

session.close()
