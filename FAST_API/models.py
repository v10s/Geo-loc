from sqlalchemy import String, Integer,Column
from sqlalchemy.orm import relationship
from uuid import UUID
from database import Base


class Location(Base):
    __tablename__ = "pin"

    key = Column(String,primary_key=True,index=True)
    latitude = Column(Integer,unique=True,index=True)
    longitude = Column(Integer)
    place_name = Column(String)
    admin_name1 = Column(String)
