from typing import List

from pydantic import BaseModel

class LocationBase(BaseModel):
    latitude : float
    longitude : float
    place_name : str
    admin_name1 : str

class LocationCreate(BaseModel):
    pass

class Location(LocationBase):
    key: str

    class Config:
        orm_mode = True
