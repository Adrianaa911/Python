from connect import *
 
# create a subroutine
def delete_films():
 
    try:
        #use filmID: is a primary and a unique field to delete a record
       # the id of the record to be deleted
        idField = input("Enter the filmID to delete a record: ")
   
        # select a record using filmId from the table
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {idField} ")
   
        row = dbCursor.fetchone() # use the fetchone() to fetch the selected record
        #None: A singleton object used to check/signal if value is absent
   
        if row == None: # row is the record returned based on the specific filmId
            print(f"No record wih the filmID {idField} exists")
            
        else: 
            dbCursor.execute(f"DELETE FROM tblFilms WHERE filmID = {idField} ")
            dbCon.commit()
            
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
   
if __name__ == "__main__":
    delete_films()
 