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

#Parse data from sara.txt
#Create a string variable that points to a copy and pasted line of data from sara.txt
lineString = "20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0"

#Create a list variable that splits lineString based on spaces and points to a list of entries from the line of data
lineData = lineString.split()

