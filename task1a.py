import pandas as pd
import textdistance
import csv
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

# Creating empty lists to store the data from csv files
abt_small_data = []
buy_small_data = []

# Opening the csv files and storing the rows in the above lists
with open('abt_small.csv',encoding='ISO-8859-1') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        abt_small_data.append(row)
with open('buy_small.csv',encoding='ISO-8859-1') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    next(readCSV)
    for row in readCSV:
        buy_small_data.append(row)
        
buy_small = pd.read_csv("buy_small.csv",encoding='ISO-8859-1')

# Creating a string consisting of the name and description of every prodcut and storing it in a list 
choices = []
for rows in buy_small_data:
    if len(rows[2])!=0:
        stri = rows[1] + rows[2]
        choices.append(stri)
    else:
        choices.append(rows[1])

# Creating an empty dictionary to store the linked ids from abt_small and buy_small csv files
data_dict = {}

# Iterating through every row representing a single product in the abt_small file
for row in abt_small_data:
    # Creating a string consisting of the name and description of every prodcut and storing it in a list 
    string = row[1] + row[2]
    
    # Choosing the best choice for pairing the ids based on the name and description 
    lists = process.extractOne(string, choices, scorer=fuzz.token_set_ratio)
    
    # Extracting the product ids from both the csv files 
    for lines in buy_small_data:
        if lines[1] in lists[0]:
            # Pairing the ids only if the similarity score is more than 70 
            if lists[1] >= 70:
                data_dict[row[0]] = lines[0]

# Separating the ids from the two files i.e. idABT and idbuy 
keys  = list(data_dict.keys())
items = list(data_dict.values())

# Converting the lists to series 
keys_series = pd.Series(keys)
items_series = pd.Series(items)

#Creating a dataframe for the paired ids from the two csv files 
frame = pd.DataFrame({'idABT': keys_series, 'idBuy': items_series})

# Producing a csv file for TASK 1
frame.to_csv('task1a.csv', index = False)
      