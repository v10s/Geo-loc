from sqlalchemy.orm import Session

import models, schemas


def get_location(db: Session,lat_:float,lng_:float):
	return db.query(models.Location).filter(models.Location.latitude == lat_, models.Location.longitude == lng_).first()




#def create_location(db: Session, loc_:schemas.LocationCreate):
#	print (loc_)
#	db_location = models.Location(**loc_.dict())
#	db.add(db_location)
#	db.commit()
#	db.refresh(db_item)
#
#	return db_location

def create_location(db: Session,key:str,latitude:float,longitude:float,place_name:str,admin_name1:str):
	db_location = models.Location(key=key,latitude=latitude,longitude=longitude,place_name=place_name,admin_name1=admin_name1)
	db.add(db_location)
	db.commit()
	db.refresh(db_location)

	return db_location


def detect(db:Session,lat_:float,lng_:float):
	result = db.query(models.Location).filter(models.Location.latitude == lat_, models.Location.longitude == lng_).first()
	return result.place_name +" , "+ result.admin_name1