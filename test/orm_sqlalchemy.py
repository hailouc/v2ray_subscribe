from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

engine = create_engine(
    "sqlite:///subscribe.vdb?check_same_thread=false",
    pool_pre_ping=True,
    pool_recycle=3600,
)


# class BaseModel(base):
#     """Base Class """
#
#     id = Column(Integer, primary_key=True, nullable=False)
#     created = Column(DateTime, nullable=False)
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'base',
#         'polymorphic_on': type
#     }


class Person(base):
    __tablename__ = "person"

    name = Column(String)

    __mapper_args__ = {
        'concrete': True
    }


base.metadata.create_all(engine)
db = sessionmaker(bind=engine)()