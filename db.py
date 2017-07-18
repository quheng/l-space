from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DB_USER = os.environ.get('DB_USER')
DB_PW= os.environ.get('DB_PW')

DB_CON_STR = f'mysql+mysqldb://{DB_USER}:{DB_PW}@localhost/testdb?charset=utf8'

engine = create_engine(DB_CON_STR, convert_unicode=True)

db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from .models import User
    Base.metadata.create_all(bind=engine)