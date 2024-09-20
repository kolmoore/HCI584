# %%
# import pandas, rename to pd
import pandas as pd

# Read books.csv file into a DataFrame (see Python refresher 4)
df = pd.read_csv('books.csv')    

# print out the dataframe (so we can check the column names)
print(df)

# Print out the column names as a list 
print(df.columns.tolist())
print(list(df))



# %%
# Simple search solution

# search for the row where the title is Unfold
row_by_title = df[df['Title'] == 'Unfold']

## print out the results
print(row_by_title)

# You will notice that we still get the column titles printed out above the row.
# Now print out the Subject of the first search result (i.e. the value of a cell in the Subject column)
# Import: In order to print out just the value of the cell, you will need to use the .values[0] method
print("Subject is:", row_by_title['Subject'].values[0])






# %%
# Solution to the book search CLI exercise
# A command line interface (CLI) for searching the books.csv file  (3 pts)

import pandas as pd
from rapidfuzz import fuzz, process

# Function to find the best a search term in the Title column
def fuzzy_find(df, search_term, n=1):
    matches = process.extract(search_term, df["Title"], scorer=fuzz.token_set_ratio, limit=n)
    first_match = matches[0] # grab only first match, ignore n for now
    text = first_match[0] # the text of the first match
    match_score = first_match[1] # the similarity score of the first match
    index = first_match[2] # the index in the data frame of the first match
    
    print(f"searched for {search_term}\nbest match: {text}, {index}, {match_score}") # DEBUG a list of tuples (text, similarity score, index)
    
    return text, index, match_score

df = pd.read_csv('books.csv')   #  read the csv file into a data frame

match_percent = 50

# %%
# input loop

# This is a good opportunity to practice using the debugger! 
# Use it to step through the loop and verify that any results look reasonable. 
# You can hover over the variables to see their values, or use the DEBUG CONSOLE to
# print out values. You can also use the DEBUG CONSOLE to run code, 
# like df.head() to see the first few rows of the data frame.

while True:

    # 1) ask the user for the title search term 
    search_term = input("What title do you want to search for? ")

    # 2) ask for a quality threshold (our match %), give it a default of 50. I the user just hits return, keep the existing value otherwise update it
    new_match_percent_str = input(f"What quality threshold do you want, currently {match_percent} ")
    if new_match_percent_str != "":
        match_percent = float(new_match_percent_str)

    # 3) search the Title column in the DataFrame df for the search term with the fuzzy search
    text, index, match = fuzzy_find(df, search_term)

    # 4) if there is a match (> 50!), print the book title, author, and year, but now nicely formatted (using a f string), like this:    
    #    `f"The summary for {title} by {author} is:\n{summary}"`
    if match > match_percent:
        row = df.iloc[index] # print the row of the best match
        print(f"The summary for {row['Title']} by {row['Author']} is:\n{row['Summary']}")
    
    # 5) if there is no good enough match, print a message saying so
    else:
        print(f"match of {match} is lower than {match_percent}, no good match found!")

    # 6) Finally ask the user if they want to search again. If they do, repeat the process. If not, exit the loop.
    new_search = input("Another Search? (y/n/)")
    if new_search.lower() == "y":
        continue
    else:
        break

