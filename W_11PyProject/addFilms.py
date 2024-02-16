from connect import *
 
# create a subroutine
def insert_films():
    # create an empty list
    film = []
    # ask for user input (MemberID, Firstname, Lastname and Email)
    # MemberID is an auto increment field and does not require input
   
    Title = input("Enter Title: ")
    yRlsd = int(input("Enter Year Released: "))
    rating = input("Enter rating film: ")
    duration = int(input("Enter duration film: "))
    genre = input("Enter Genre: ")
    print(f"Data: {Title, yRlsd, genre}")
    # append data Title, yRlsd and genre
   
    film.append(Title)
    film.append(yRlsd)
    film.append(rating)
    film.append(duration)
    film.append(genre)
    print(f"The film list {film}")
 
    "INSERT INTO tblfilms VALUES(NULL, 'A','B','C','D','E','F')"
    "INSERT INTO tblfilms (filmId, Title, yRlsd, rating, duration, genre) VALUES( 'A','B','C','D','E','F')"
 
    try:
        dbCursor.execute("INSERT INTO tblfilms ( title, yearReleased, rating, duration, genre) VALUES(?,?,?,?,?)", film) # Values from the list
        # or
        # values directly from variables
        # dbCursor.execute("INSERT INTO tblfilms VALUES(NULL, ?,?,?)", (filmID,Title,yRlsd,genre, rating, duration))
        dbCon.commit() # make the changes permanent
        print(f"{Title} inserted in the Table")
    except sql.OperationalError as e:
        dbCon.rollback()
        print(f"Insert failed {e}")
if __name__== "__main__":
    insert_films()