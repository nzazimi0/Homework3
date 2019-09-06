#!/usr/bin/env python
# coding: utf-8

# In[55]:


import os
import csv

PyBank_csv = 'budget_data.csv'
#print(PyBank_csv)
#Read in the CSV file
with open(PyBank_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    # Prompt the user for what wrestler they would like to search for

    # name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    Month=0
    NetProfit=0
    Delta_List=[]
    Counter=1
    
    Max_delta=0
    Min_delta=0
    for row in csvreader:
        Month=Month+1
        NetProfit=NetProfit+int(row[1])
        #print (row)
        if Counter==1:
            Change=int(row[1])
        else:   
            Delta=int(row[1])-Change
            Delta_List.append(Delta)
            if Delta> Max_delta:
                Max_delta=Delta
                Final_Max_Date=row
            
            if Delta< Min_delta:
                Min_delta=Delta
                Final_Min_Date=row
            
        
        Counter=Counter+1
        Change=int(row[1])

                
print (Month)
print (NetProfit)
print (sum(Delta_List)/len(Delta_List))
print (Final_Max_Date[0],max(Delta_List))
print (Final_Min_Date[0],min(Delta_List))
