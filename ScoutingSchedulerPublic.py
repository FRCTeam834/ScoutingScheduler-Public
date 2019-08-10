# Author: Mohammad Durrani
# Date: Friday, August 9th, 2019
# Special Thanks: Dalton from FRC 66, Tyler from WPILip and 3512, Tim from 1257, and FRC Discord


import gspread
    #Google sheets API client thing
from oauth2client.service_account import ServiceAccountCredentials
    #Authenticating accsess to google


#++++++++++++++++++++ Google Authentication ++++++++++++++++++++#

#printing debug message
print("Authenticating to Google Sheets/Google...\n\n")

#setting scope (do not change)
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

#setting credentials and authorizing credentials
creds = ServiceAccountCredentials.from_json_keyfile_name("##########.json", scope)
gc = gspread.authorize(####)

#opening worksheet and sheet1
wks = gc.open("############").sheet1

#finishing debug message
print("Done!\n\n")

#++++++++++++++++++++ Google Authentication ++++++++++++++++++++#



#++++++++++++++++++++ Declaring Variables ++++++++++++++++++++#
scoutingGroup = 0
counter = 0
groupNumCounter = 1
scoutingCounter = 0
numMatchesPerGroup = 0
numMatchesCounter = 10
qualCounter = 0
#++++++++++++++++++++ Declaring Variables ++++++++++++++++++++#



#++++++++++++++++++++ Clearing Previous Schedule ++++++++++++++++++++#
#debug message
print("Deleting previous schedule...\n\n")

#setting the range to delete
delete = wks.range('A2:B200')

#iterating through and deleting cells
for cell in delete:
    cell.value = ""

#Batch update to delete
wks.update_cells(delete)

#end debug message
print("Done!\n\n")
#++++++++++++++++++++ Declaring Variables ++++++++++++++++++++#



#++++++++++++++++++++ User Input ++++++++++++++++++++#
qualMatches = int(input("Enter the number of qualification matches: "))
scouts = int(input("Enter the number of scouts (total): "))
scoutsInGroup = int(input("How many people do you want scouting at a time: "))
#++++++++++++++++++++ User Input ++++++++++++++++++++#



#++++++++++++++++++++ Calculations ++++++++++++++++++++#

    #Finding how many matches each group will scout

#while the number of matches they are scouting is greater than 5 (Change this and the if statment outside of the while loop to lower the minimmum matches)
while numMatchesCounter > 5:

    #if the number of matches goes in cleanly (no decimals) and if so break and set the number of matches per group. otherwise, move the nummatch counter lower
    if qualMatches % numMatchesCounter == 0:
        numOfMatchPerGroup = numMatchesCounter
        break
    else:
        numMatchesCounter -= 1

#if the number of matches per group have moved below 5, print error
if numMatchesCounter < 5:
    print("no work")

    #Finding how many matches each group will scout

#calculation the number of groups
groups = scouts / scoutsInGroup
# ************BIG CALCULATIONS*********


#++++++++++++++++++++ Moving the Data into Arrays ++++++++++++++++++++#

#initializing qualification lists
qualList = []

#iterating the qualmatches into a list
for x in range(qualMatches):
    {
        #adding the qualification matches
        qualList.append("Qualification Match " + str(x + 1))
    }

#initializing the scouting group list
scoutingList = []

scoutingCounter=0 #idk why i have this here
#while there are still qualification matches
while counter < (qualMatches + 1):

    #while the scouting counter is less than the number of matches scouted per group
    while scoutingCounter < (numOfMatchPerGroup):

        #adding the scout groups to the list and incrementing the scouting counter
        scoutingList.append("Group " + str(groupNumCounter))
        scoutingCounter += 1

    #if the maximum number of groups is met, revert back to one, if not,  increase the group number
    if groupNumCounter == groups:

        groupNumCounter = 1

    else:
        groupNumCounter += 1

    scoutingCounter = 0
    counter += 1
#++++++++++++++++++++ Moving the Data into Arrays ++++++++++++++++++++#



#++++++++++++++++++++ Yeeting the Data to Google Sheets ++++++++++++++++++++#
#setting a cell range for the qualification matches
cell_list = wks.range("A2:A"+str(qualMatches+1))

#iterating through cells to put in the qualification matches
for cell in cell_list:

    #setting the cell values to qualList and incrasing the counter
    cell.value = qualList[qualCounter]
    qualCounter+=1

# Update in batch
wks.update_cells(cell_list)

#setting a cell range for the scouting groups
cell_list2 = wks.range("B2:B"+str(qualMatches+1))

#iterating through cells to put in the scouting groups
for cell in cell_list2:

    #setting through cells value to scoutingList and increasing the counter
    cell.value = scoutingList[qualCounter]
    qualCounter+=1

# Update in batch
wks.update_cells(cell_list2)
#++++++++++++++++++++ Yeeting the Data to Google Sheets ++++++++++++++++++++#