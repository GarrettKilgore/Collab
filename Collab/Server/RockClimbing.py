import sqlite3

def dict_factory(cursor, row):
 fields = []
 # Extract column names from cursor description
 for column in cursor.description:
    fields.append(column[0])

 # Create a dictionary where keys are column names and values are row values
 result_dict = {}
 for i in range(len(fields)):
    result_dict[fields[i]] = row[i]

 return result_dict

class RockClimbingDB:
   
   def __init__(self, filename):
      #connect to DB file
      self.connection = sqlite3.connect(filename)
      self.connection.row_factory = dict_factory
      #use the connection instance to perform db operations
      #create a curso instance for the connection
      self.cursor = self.connection.cursor()

   def getRockClimbings(self):
        #now that we have an access point we can fetch all or one
        #ONLY applicable use of fetch is following a SELECT query
        self.cursor.execute("SELECT * FROM rockclimbing")
        rockclimbings = self.cursor.fetchall()
        print("Get Statement", rockclimbings)
        return rockclimbings
    
   def getRockClimbing(self, climbing_id):
        data = [climbing_id]
        self.cursor.execute("SELECT * FROM rockclimbing WHERE id = ?", data)
        rockclimbing = self.cursor.fetchone()
        return rockclimbing
   
   def createRockClimbing(self, name, review, rating):
        data = [name,review,rating]
        #add a new rockclimb to our db
        self.cursor.execute("(INSERT INTO rockclimbing(name, review, rating)VLAUES(?,?,?)", data)
        self.connection.commit()

   def updateRockClimbing(self,climbing_id,name,review,rating):
       data = [name, review, rating, climbing_id]
       self.cursor.execute("UPDATE rockclimbing SET name = ?, review = ?, rating = ? WHERE id = ?", data)
       self.connection.commit()