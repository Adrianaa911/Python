from connect import * 

# create a subroutine
def update_films():
 
    
    try:
        #  the id of the record to be updated 
        idField = input("Enter the filmID to update a record: ")

        # select a record using filmId from the table
        dbCursor.execute(f"SELECT * FROM tblfilms WHERE filmId = {idField} ")

        row = dbCursor.fetchone() # use the fetchone() to fetch the selected record
        #None: A singleton object used to check/signal if value is absent
        if row == None: # row is the record returned based on the specific MemberID
            print(f"No record wih the filmId {idField} exists")
        
        else:
            # the field selected for update 
            fieldTitle = input("Enter the field (Title or YearReleased or Genre) to update: ")

            # the value to be entered in the field 
            fieldValue = input(f"Enter the value for the {fieldTitle}: ")

            # add quotes to field value 
            fieldValue = "'"+fieldValue+"'"

             # UPDATE tblfilms SET Title = "Now you see me" WHERE filmId = 1/2/3/4....
            #use filmId is a primary and a unique field to update a record
            dbCursor.execute(f"UPDATE tblFilms SET {fieldTitle} = {fieldValue} WHERE filmId = {idField} ")
            dbCon.commit()
            print(f"{idField} Updated in the tblFilms table ")
    except sql.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_films()

