# Program Info
# Creator: Deep Nayak
# Purpose: To populate a MySQL database for the NextBinge project by reading data from a CSV file.
# Language: Python 3.8.1
# Last Edit: 29/09/2020

# Importing all the necessary libraries
import mysql.connector, ast, csv, itertools, datetime

# /////////////IMPORTANT/////////////
# Enter your MySQL password between the quotes below
mysqlpass = ""
# Opening the CSV file in read mode.
rawcsv = csv.reader(open('NextBingeCSV.csv', "r", encoding="utf-8", errors='ignore'), delimiter=",")

# Skipping the headers
rawcsv.__next__()

# Defining separate sets for each table records
prodvalues = set()
actorvalues = set()
directorvalues = set()
castvalues = set()
movievalues = set()
charactervalues = set()
detailsvalues = set()
cast_id = 1

# Writing the SQL queries for each insert statement
actorinsert = "INSERT INTO actor (actor_id, name, gender) VALUES (%s, %s, %s)"
directorinsert = "INSERT INTO director (director_id, name, gender) VALUES (%s, %s, %s)"
prodinsert = "INSERT INTO production_house (production_id, name) VALUES (%s, %s)"
castinsert = "INSERT INTO cast (cast_id, actor_id, director_id, production_id) VALUES (%s, %s, %s, %s)"
movieinsert = "INSERT INTO movie (movie_id, cast_id, movie_name) VALUES (%s, %s, %s)"
detailsinsert = "INSERT INTO details (movie_id, genre, description, runtime, release_date, popularity, vote_average, vote_count) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
characterinsert = "INSERT INTO movie_character (movie_id, actor_id, char_name) VALUES (%s, %s, %s)"

# Scanning the CSV file row by row
for row in rawcsv:
	# Creating a list of ids for the particular row
	actoridset = []
	prodidset = []
	directoridset = []
	genres = []

	# Converting the given string of list of dictionaries to its python equivalent
	pyrow1 = ast.literal_eval(row[0])
	for genre in pyrow1:
		genres.append(genre["name"])
	movie_id = int(row[1])
	description = row[2]
	popularity = float(row[3])

	prodhouses = []
	pyrow2 = ast.literal_eval(row[4])
	for prodhouse in pyrow2:
		prodvalues.add((prodhouse["id"], prodhouse["name"]))
		prodidset.append(prodhouse["id"])

	# Checking the format of the release date
	try:
		release_date = datetime.datetime.strptime(row[5], '%m/%d/%Y').strftime('%Y-%m-%d')
	except ValueError:
		release_date = datetime.datetime.strptime(row[5], '%m-%d-%Y').strftime('%Y-%m-%d')
	runtime = row[6]
	movie_name = row[7]
	vote_average = float(row[8])
	vote_count = float(row[9])

	pyrow3 = ast.literal_eval(row[10])
	for actor in pyrow3:
		actorvalues.add((actor["id"], actor["name"], actor["gender"]))
		charactervalues.add((movie_id, actor["id"], actor["character"]))
		# desclen = max(desclen, len(actor["character"]))
		actoridset.append(actor["id"])
	
	pyrow4 = ast.literal_eval(row[11])
	for director in pyrow4:
		# Checking if the current dictionary contains a director
		if director["job"] == "Director":
			directorvalues.add((director["id"], director["name"], director["gender"]))
			directoridset.append(director["id"])

	for combo in itertools.product(actoridset, directoridset, prodidset):
		castvalues.add((cast_id, *combo))
		movievalues.add((movie_id, cast_id, movie_name))
		cast_id += 1

	# Adding the remaining values in the details set
	detailsvalues.add((movie_id, ','.join(genres), description, runtime, release_date, popularity, vote_average, vote_count))

# Inserting data one by one for each table by first creating a connection
# Creating a cursor, inserting values and finally closing the cursor and connection
mydb1 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor1 = mydb1.cursor()
mycursor1.executemany(actorinsert, actorvalues)
mydb1.commit()
mycursor1.close()
mydb1.close()
print("Actor done.")

mydb2 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor2 = mydb2.cursor()
mycursor2.executemany(directorinsert, directorvalues)
mydb2.commit()
mycursor2.close()
mydb2.close()
print("Director done.")

mydb3 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor3 = mydb3.cursor()
mycursor3.executemany(prodinsert, prodvalues)
mydb3.commit()
mycursor3.close()
mydb3.close()
print("Prod done.")

mydb4 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor4 = mydb4.cursor()
mycursor4.executemany(castinsert, castvalues)
mydb4.commit()
mycursor4.close()
mydb4.close()
print("Cast done.")

mydb5 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor5 = mydb5.cursor()
mycursor5.executemany(movieinsert, movievalues)
mydb5.commit()
mycursor5.close()
mydb5.close()
print("Movie done.")

mydb6 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor6 = mydb6.cursor()
mycursor6.executemany(detailsinsert, detailsvalues)
mydb6.commit()
mycursor6.close()
mydb6.close()
print("Details done.")

mydb7 = mysql.connector.connect(
	host="localhost",
	user="root",
	password=mysqlpass,
	database="nextbinge"
)
mycursor7 = mydb7.cursor()
mycursor7.executemany(characterinsert, charactervalues)
mydb7.commit()
mycursor7.close()
mydb7.close()
print("Character done.")

# If the code executes successfully upto this point, the data has been successfully populated in the respective tables.