from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import crud, models, schemas
from database import SessionLocal, engine
from geopy import distance
import math
import pytest


models.Base.metadata.create_all(bind=engine)
app = FastAPI(debug=True)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.post("/post_location", response_model=schemas.Location)
def create_location(pin:str,latitude:float,longitude:float,place_name:str,admin_name1:str, db: Session = Depends(get_db)):
	return crud.create_location(db=db,key=pin,latitude=latitude,longitude=longitude,place_name=place_name,admin_name1=admin_name1)


@app.get("/get_location")
def get_location(lat__: float,lng__: float,db:Session = Depends(get_db)):
	return crud.get_location(db=db,lat_=lat__,lng_=lng__)

@app.get("/get_using_postgre")
def fetch_by_postgres(lat_:float,lng_:float,db:Session = Depends(get_db)):
	query = "SELECT * FROM pin WHERE earth_box(ll_to_earth("+str(lat_)+","+str(lng_)+"), 5000) @> ll_to_earth(latitude,longitude); "


	conn = engine.connect()
	result = conn.execute(query)

	conn.close()
	final = ""
	
	for row in result:
		final += final +" "+ str(row)
	if final == "":
		return "No results found."

	return final
	
	


@app.get("/get_using_self")
def fetch_by_self(lat_:float,lng_:float):

	rad = 5 # search radi
	Radi_earth = 6371
	maxLat = lat_ + math.degrees(rad/Radi_earth);
	minLat = lat_ - math.degrees(rad/Radi_earth);
	maxLon = lng_ - math.degrees(math.asin(rad/Radi_earth) / math.cos(math.degrees(lat_)));
	minLon = lng_ + math.degrees(math.asin(rad/Radi_earth) / math.cos(math.degrees(lat_)));

	print("latitude : "+str(maxLat)+" , "+str(minLat))
	
	print("longitude : "+str(maxLon)+" , "+str(minLon))

	query = "Select * From pin Where latitude Between "+str(minLat)+" And "+str(maxLat)+" And longitude Between "+str(minLon)+" And "+str(maxLon)+";"
	
	conn = engine.connect()
	result = conn.execute(query)

	conn.close()
	final = ""
	
	for row in result:
		print(row)
		final += final +" "+ str(row)

	if final == "":
		return "No results found."

	return final
	
	


@app.get("/detect")
def detect(lat__:float,lng__:float,db:Session = Depends(get_db)):
	return crud.detect(db=db,lat_=lat__,lng_=lng__)
	