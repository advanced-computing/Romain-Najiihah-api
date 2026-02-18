# Trial API
@film_permits.get("/")
@film_permits.get("/api/list")

Inspired or cipied from the exmaples, we were trying to understand how thing were working. 
The first one, just check that the API is running. 
The second one can filter through columns. 

# our API
@film_permits.get("/api/record/<record_id>")

This API requires to input the unique EVENT_ID for each row and will return the row. 