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
    
 #   print(f"searched for {search_term}\nbest match: {text}, {index}, {match_score}") # DEBUG a list of tuples (text, similarity score, index)
    
    return text, index, match_score

df = pd.read_csv('books.csv')   #  read the csv file into a data frame
init = 1
thresh = 50

while True:

    # 1) ask the user for the title search term only use this on the initial search and then use follow up search
    while init: 
        title = input('Hello welcome to our book searching tool! \nWhat title can we look up for you today? ')
        init = 0

    # 2) ask for a quality threshold (our match %), give it a default of 50. I the user just hits return, keep the existing value otherwise update it
    new_thresh = input(f"Current Result Threshold: {thresh}%  \nEnter new threshhold or press enter to retain current ")
    if new_thresh != '':
        thresh = float(new_thresh)

    # 3) search the Title column in the DataFrame df for the search term with the fuzzy search 

    text, index, match = fuzzy_find(df, title)


    # 4) if there is a match (> 50!), pull out book title, author, and year, 
    #    and print the but now nicely formatted (using a f string), like this:    
    #       title, author, summary = row["Title"], row["Author"], row["Summary"]
    #       print(f"The summary for {title} by {author} is:\n{summary}")

    if match > thresh:
        row = df.iloc[index] # find the row of the best match
        title, author, summary = row["Title"], row["Author"], row["Summary"][:200]
        print(f"\nThe summary for \033[1m{title}\033[0m by {author} starts with:\n\n{summary}\n\n")
    else:
        print('Uh No! No good match found.  \nEither try a different title or turn down the threshold for more flexibility in the results. \n\n')
    
    # 5) if there is no good enough match, print a message saying so

    # 6) Finally ask the user if they want to search again. If they do, repeat the process. If not, exit the loop.
    title = input('Enter new title to search or hit enter to quit: ')
    if title == '':
        print("\nThanks for searching! Goodbye")
        break



# Note: this is a good opportunity to practice using the debugger! 
# Use it to step through the loop and verify that any results look reasonable. 
# You can hover over the variables to see their values, or use the DEBUG CONSOLE to
# print out values. You can also use the DEBUG CONSOLE to run code, 
# like `df.head()` to see the first few rows of the data frame.

