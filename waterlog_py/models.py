from sqlalchemy import (
    Column,
    Index,
    Integer,
    SmallInteger,
    BigInteger,
    Float, 
    Text,
    String
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class WaterLoggingInfo(Base):
    """docstring for WaterLoggingInfo"""
    __tablename__ = 'water_logging_info'
    id = Column(Integer, primary_key=True)
    android_id = Column(String(100))
    lat = Column(Float) 
    long = Column(Float) 
    logging_level = Column(SmallInteger)