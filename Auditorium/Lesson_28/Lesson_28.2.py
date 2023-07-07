from sqlalchemy import create_engine, Integer, String, Column, MetaData, Table, DateTime, ForeignKey, Numeric, SmallInteger
from sqlalchemy.orm import declarative_base, Session, sessionmaker, relationship
from datetime import datetime
from sqlalchemy_utils import create_database, database_exists

engine = create_engine("postgresql+psycopg2://postgres:Antaris7@localhost:5432/sqlalchemy_tuts")
#if not database_exists(engine.url):
    #create_database(engine.url)

session = Session(bind=engine)

Base = declarative_base()
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#Base.metadata.create_all(engine)
c1 = Customer(first_name = 'Jason', last_name = 'Tyler', username = 'Jason_Tyler', email = 'Jason_Tyler@gmail.com')
session.add(c1)
print(session.new)
session.commit()