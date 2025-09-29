#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Sameer Swarup (sameer.swarup@duke.edu)
# Date:   Fall 2025
#--------------------------------------------------------------
#Create a variable pointing to the data file
file_name = r"V:\VSCodeTest\TurtleTrackingProject\data\raw\Sara.txt"

#Create a file object from the file
file_object = open(file_name,'r')

#Full path: "V:\VSCodeTest\TurtleTrackingProject\data\raw\Sara.txt"

#Read contents of file into a list, one line at a time
line_list = file_object.readlines()

#Close the file
file_object.close()

#Parse data from sara.txt
#Iterate through all data lines in Sara.txt
for lineString in line_list:
    #Create a list variable that splits lineString based on spaces and points to a list of entries from the line of data
    lineData = lineString.split()
    if lineData[0] in ['#', 'u']:
        continue
    # Assign variables to specfic items in the list
    record_id = lineData[0]  # ARGOS tracking record ID
    obs_date = lineData[2] # Observation date
    ob_lc = lineData[4]      # Observation Location Class
    obs_lat = lineData[6]    # Observation Latitude
    obs_lon = lineData[7]    # Observation Longitude

    #Print the location of sara
    #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat},lon:{obs_lon} on {obs_date}")