import os
import csv

PyPoll_csv = 'election_data.csv'
#print(PyBank_csv)
#Read in the CSV file
with open(PyPoll_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    Vote=0
#     NetProfit=0
    Candidate_List=[]
    Khan=0
    Correy=0
    Li=0
    OTooley=0

    for row in csvreader:
        Vote=Vote+1
        
        if row[2] not in Candidate_List:
             Candidate_List.append(row[2])
        if row[2]=='Khan':
            Khan=Khan+1
        if row[2]=='Correy':
            Correy=Correy+1
        if row[2]=='Li':
            Li=Li+1
        if row[2]=='O\'Tooley':
            OTooley=OTooley+1

Votes_Count={'Khan':Khan,'Correy':Correy,'Li':Li,'O\'Tooley':OTooley}                
print (Vote)
print (Candidate_List)
print (Khan,Correy,Li,OTooley)
print (round (100*Khan/Vote,3),100*Correy/Vote,100*Li/Vote,100*OTooley/Vote)

Votes_Count

