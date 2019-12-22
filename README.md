# test
## A geolocation app</h3>

#### Requirements
* * Uvicorn * *
* * postgres * *
* * postgis * *

#### How to setup :
```
First run the ./sql/main.sql on your postgres db
```
```
Load the ./sql/IN.csv to your db in the pin table
```
```
NOW run the ./sql/json_load.sql file.
```
###### Now you are ready to use and implement on the uvicorn server

#### Testing
The testing file is ./testmain.py . 
And contains all the test case to check the functioning of all api path functions.
