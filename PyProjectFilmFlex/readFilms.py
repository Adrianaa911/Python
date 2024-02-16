from connect import *
 
# create a subroutine
def read_films():
    try:  # select all records from the table
        
        # Method 1 
        #dbCursor.execute("SELECT * FROM tblfilms")
        # fetchall(): fetehes all the the selected records
        #rows = dbCursor.fetchall()# row holds alll fetched records
       # or
       
       #  Method 2
       
        rows = dbCursor.execute("SELECT * FROM tblfilms").fetchall()
 
        if not rows: # row is the record returned based on the specific MemberID
            print(f"No record(s) exists")
        # loop through all the records in the row variable
        else:
            for aRecord in rows:
                # print all record
                print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")
if __name__ == "__main__":
    read_films()