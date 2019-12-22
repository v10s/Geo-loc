CREATE EXTENSION IF NOT EXISTS "cube";

CREATE EXTENSION IF NOT EXISTS "earthdistance";


/* must set successfully install the postgis in your postgres server to run */
CREATE EXTENSION IF NOT EXISTS "postgis";



CREATE TABLE pin ( key CHAR(10) PRIMARY KEY , place_name VARCHAR(50) NOT NULL,admin_name1 VARCHAR(50) NOT NULL, latitude double precision ,longitude double precision ,accuracy double precision);
