from connect import *
import logging
import time
filename = __file__
 
logging.basicConfig(filename=r"Python\W_11PyProject/file1.log", level=logging.DEBUG)
 
# create a subroutine
def search():
    try:
        field = input("Would you like to search by title or genre or filmID or yearReleased or duration or rating? ")
        if field == "title" or field == "genre" or field == "rating":
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE '%{searchInput}%'")
            # dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} = '{searchInput}'")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with field {field} Matching '{searchInput} ' in the table ")
                
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {searchInput} as {field}")
 
            else:
                for aRecord in rows:
                    print(aRecord)

        
        elif field == "filmID" or field == "yearReleased" or field == "duration":
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM tblFilms WHERE {field} LIKE {searchInput}")
            rows = dbCursor.fetchall()
            if not rows:
                print(f"No record with {field} exists in the table: ")
                # print(f"No record with field {field} Matching '{searchInput} ' in the table ")
            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search filed {field}")
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
if __name__ == "__main__":
    search()
    
    
    
    # https://stackoverflow.com/questions/533048/how-to-log-source-file-name-and-line-number-in-python