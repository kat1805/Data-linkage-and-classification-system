import pandas as pd
import textdistance
import csv
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from nltk.tokenize import sent_tokenize, word_tokenize
from fuzzywuzzy import process
from fuzzywuzzy import fuzz

# Reading the csv files 
buy = pd.read_csv("buy.csv",encoding='ISO-8859-1')
abt = pd.read_csv("abt.csv",encoding='ISO-8859-1')

# Creating an empty dictionary to store the blocks for the ids in the buy.csv file
dit = {}

# Grouping the products by their names 
group_name = buy.groupby('name')

# Finding the blocks for the products in the buy.csv file 
# Blocking the products by the product names first and then by the manufacturer name
for block in list(group_name.groups.keys()):
        group_block = group_name.get_group(block)
        group_manu = group_block.groupby('manufacturer')
        for value in list(group_manu.groups.keys()):
            manu_block = group_manu.get_group(value)
            
            # Storing the id and the associated block name in a dictionary 
            for ids in manu_block['idBuy']:
                dit[ids] = value

# Creating an empty list to store the manufacturer names for the products in the abt.csv file   
abt_manufact = []

# Finding the manufacturer names for the prodcuts in the abt.csc file  
for line in abt['name']:
    tokens = word_tokenize(line)
    abt_manufact.append(tokens[0])

# Storing the ids for the products in the abt.csv file 
abt_ids = [ids for ids in abt['idABT']]

# Creating an empty dictionary to store the blocks and the ids 
dit_abt = {}

# By using the blocks found using the buy.csv file, blocking the products in the buy.csv file 
i=0
while i<len(abt_ids): 
    t = process.extractOne(abt_manufact[i], list(dit.values()), scorer=fuzz.token_set_ratio)
    
    # Storing the ids and the associated blocks in a dictionary 
    dit_abt[abt_ids[i]] = t[0]
    i = i + 1

# Converting the dictionary consisting of the blocks and product ids from the abt.csv file to a dataframe
abt_ids_series = pd.Series(list(dit_abt.keys()))
abt_blocks_series = pd.Series(list(dit_abt.values()))
abt_df = pd.DataFrame({'block_key': abt_blocks_series, 'product_id': abt_ids_series})

# Converting the dataframe to a csv file 
abt_df.to_csv('abt_blocks.csv', index = False)

# Converting the dictionary consisting of the blocks and product ids from the abt.csv file to a dataframe
buy_ids_series = pd.Series(list(dit.keys()))
buy_blocks_series = pd.Series(list(dit.values()))
buy_df = pd.DataFrame({'block_key': buy_blocks_series, 'product_id': buy_ids_series})

# Converting the dataframe to a csv file 
buy_df.to_csv('buy_blocks.csv', index = False)     