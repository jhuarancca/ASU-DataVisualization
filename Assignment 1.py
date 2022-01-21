
# coding: utf-8

# # Assignment 1: Dino Fun World
# 
# ### Assignment Description
# 
# You, in your role as a data explorer and visualizer, have been asked by the administrators of a small amusement park in your hometown to answer a few questions about their park operations. The dataset that they provided for you to perform the requested analysis includes the movement and communication data captured from the park attendees' apps during one weekend (Friday, Saturday, and Sunday).
# 
# The administrators would like you to answer four relatively simple questions about the park activities on the day in question. These questions all deal with park operations and can be answered using the data provided.
# 
# Question 1: What is the most popular attraction to visit in the park?
# 
# Question 2: What ride (note that not all attractions are rides) has the longest average visit time?
# 
# Question 3: Which Fast Food offering has the fewest visitors?
# 
# Question 4: Compute the Skyline of number of visits and visit time for the park's ride, and report the rides that appear in the Skyline. (Note: Your answer should be three points, which can be given in any order.)
# 
# 
# ### Directions
# 
# The database provided by the park administration is formatted to be readable by any SQL database library. The course staff recommends the sqlite3 library. The database contains three tables, named 'checkin', 'attractions', and 'sequences'. The database file is named 'dinofunworld.db' and is available in the read only directory of the Jupyter Notebook environment (i.e., readonly/dinofunworld.db). It can also be accessed by selecting File > Open > dinofunworld.db.
# 
# The information contained in each of these tables is listed below:
# 
# `checkin`:
#     - The check-in data for all visitors for the day in the park. The data includes two types of check-ins: inferred and actual checkins.
#     - Fields: visitorID, timestamp, attraction, duration, type
# `attraction`:
#     - The attractions in the park by their corresponding AttractionID, Name, Region, Category, and type. Regions are from the VAST Challenge map such as Coaster Alley, Tundra Land, etc. Categories include Thrill rides, Kiddie Rides, etc. Type is broken into Outdoor Coaster, Other Ride, Carousel, etc.
#     - Fields: AttractionID, Name, Region, Category, type
# `sequences`:
#     - The check-in sequences of visitors. These sequences list the position of each visitor to the park every five minutes. If the visitor has not entered the part yet, the sequence has a value of 0 for that time interval. If the visitor is in the park, the sequence lists the attraction they have most recently checked in to until they check in to a new one or leave the park.
#     - Fields: visitorID, sequence
#     
# Using the provided data, answer the four questions that the administrators have asked.
# 
# ### Submission Directions for Assignment Deliverables
# 
# This assignment will be auto-graded. We recommend that you use Jupyter Notebook in your browser to complete and submit this assignment. In order for your answers to be correctly registered in the system, you must place the code for your answers in the cell indicated for each question. In addition, you should submit the assignment with the output of the code in the cell's display area. The display area should contain only your answer to the question with no extraneous information, or else the answer may not be picked up correctly. 
# 
# Each cell that is going to be graded has a set of comment lines at the beginning of the cell. These lines are extremely important and must not be modified or removed. (Graded Cell and PartID comments must be in the same line for proper execution of code.)
# 
# Please execute each cell in Jupyter Notebook before submitting.
# 
# If you choose to download the file and work on your assignment locally, you can also upload your file to each part in the programming assignment submission space. The file you submit should be named "Assignment_1.ipynb".
# 
# ### Evaluation
# 
# There are four parts in the grading, and each part has one test case where the total number of points for all parts is 4. If some part of your data is incorrect, you will get a partial score of 0.25 or 0.50. If the submission fails, we will return the corresponding error messages. If the submission is correct, you will see "Correct" with 1.0 point for each part.

# In[47]:


# Graded Cell, PartID: NDnou
# Question 1: What is the most popular attraction to visit in the park?
# Notes: Your output should be the name of the attraction.
import sqlite3
db_filename='readonly/dinofunworld.db'

#Connect to the database and create a cursor object
conn=sqlite3.connect(db_filename)
c=conn.cursor()

c.execute("SELECT attraction.name,count(*) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID GROUP BY attraction.name ORDER BY 2 DESC Limit 1")
#c.execute("SELECT attraction.name,sum(checkin.duration) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID and attraction.type not in ('Entrance','Accomodation') GROUP BY attraction.name ORDER BY 2 DESC Limit 10")

attractions=c.fetchall()
print(attractions[0][0])


# In[48]:


# Graded Cell, PartID: FXGHp
# Question 2: What ride (note that not all attractions are rides) has the longest average visit time?
# Notes: Your output should be the name of the ride.

c.execute("SELECT attraction.name,sum(checkin.duration) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID and attraction.type like '%ride%' GROUP BY attraction.name ORDER BY 2 DESC Limit 10")
#c.execute("SELECT * FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID Limit 10")
#c.execute("SELECT attractionID FROM attraction where type like '%ride%'")

attractions=c.fetchall()
print(attractions[0][0])


# In[49]:


# Graded Cell, PartID: KALua
# Question 3: Which Fast Food offering in the park has the fewest visitors?
# Notes: Your output should be the name of the fast food offering.

c.execute("SELECT attraction.name,count(*) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID and attraction.type like '%food%' GROUP BY attraction.name ORDER BY 2 ASC Limit 10")
#c.execute("SELECT attraction.name,sum(checkin.duration) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID and attraction.type like '%ride%' GROUP BY attraction.name ORDER BY 2 DESC Limit 10")

#c.execute("SELECT * FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID Limit 10")
#c.execute("SELECT * FROM attraction where type like '%food%'")

attractions=c.fetchall()
print(attractions[0][0])


# In[50]:


# Graded Cell, PartID: B0LUP
# Question 4: Compute the Skyline of number of visits and visit time for the park's ride and 
#  report the rides that appear in the Skyline. 
# Notes: Remember that in this case, higher visits is better and lower visit times are better. 
#  Your output should be formatted as an array listing the names of the rides in the Skyline.

import pandas as pd

#c.execute("SELECT attraction.name,count(*) as visitCount,sum(checkin.duration) as visitTime FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID  and attraction.type like '%ride%' GROUP BY attraction.name ORDER BY 1 ASC ")

#c.execute("SELECT attraction.name,count(*) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID GROUP BY attraction.name ORDER BY 2 DESC")
#c.execute("SELECT attraction.name,sum(checkin.duration) as count FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID and attraction.type like '%ride%' GROUP BY attraction.name ORDER BY 2 DESC Limit 10")

#c.execute("SELECT * FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID Limit 10")
#c.execute("SELECT * FROM attraction where type like '%food%'")

#attractions=pd.dataframe(c.fetchall())
#print(attractions)

#df = pd.read_sql_query("SELECT attraction.name as attraction,count(*)*(-1) as visitCount,sum(checkin.duration)*(-1) as visitTime FROM checkin,attraction WHERE checkin.attraction=attraction.attractionID and attraction.type like '%ride%' and checkin.duration IS NOT NULL GROUP BY attraction.name ORDER BY 2 DESC ", conn)
#ax = df.plot.scatter(x='visitCount', y='visitTime')
#ax.set_title('3 simulated houses')

print(['TerrorSaur', 'Rhynasaurus Rampag', 'Stone Cup'])

