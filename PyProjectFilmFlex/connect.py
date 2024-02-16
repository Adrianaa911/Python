import sqlite3 as sql # import the standard sqlite3 module


try: 
    # To use the module, start by creating db connection object (variable to hold the folder/file)
    with sql.connect("Python/W_11PyProject/filmflix.db") as dbCon:
        #once the connection and/or dbfile is created
        #create a cursor object(variable) called dbcursorand call it cursor method  
        dbCursor = dbCon.cursor() # use to execute sql statements

except sql.OperationalError as e: # raise sql error
    # handle the exception/error raised 
    print(f"Connection failed: {e}") # tells what the error is
    