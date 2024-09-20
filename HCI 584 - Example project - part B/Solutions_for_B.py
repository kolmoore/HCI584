# %%
# TkInter widgets I will need and for what function:
#
# - using a text entry field, the user enters a search term (for the title)
# - to the left is a label "Search for Title"
# - Optional: in the line below: a label Quality Threshold and 1 to 100 slider (default 50)
# - the search results are displayed in a Text widget (i.e. a multi-line text field, similar to a terminal window), which the user can copy from but not edit. As the text can be quite long, we'll use a scrolled Text widget
# - For now, it will just display title, author and summary 

# %%
# see GUI_sketch_Chris.png

# load and display GUI_sketch_Chris.png
from PIL import Image
Image.open("GUI_sketch_Chris.png")

# %%
# My solution for GUI with a init and start_search method
import tkinter as tk

class Ebook_app(tk.Tk): # Inherit from tk.Tk, so can later use mainloop()
    def __init__(self):
        super().__init__() # Call the __init__() method of the parent class tk.Tk
        self.title("Ebook Search") # Set the title of the window

        # Create a Label
        self.label = tk.Label(self, text="Search for Title:")
        self.label.pack(pady=10)  # pad by 10 pixels

        # Create an Entry Widget
        self.entry = tk.Entry(self)
        self.entry.pack()

        # Create a Start Search Button
        self.search_button = tk.Button(self, text="Start Search", command=self.start_search)
        self.search_button.pack(pady=10)

    def start_search(self):
        search_text = self.entry.get() # Get the text from the Entry Widget
        print(f"Searching for: {search_text}")

app = Ebook_app()
app.mainloop()

# %%
# My solution for using grid for a better layout
import tkinter as tk

class Ebook_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ebook Search")

        # Create a Label and place it on the left (column 0)
        self.label = tk.Label(self, text="Search for Title:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Create an Entry Widget and place it in the middle (column 1)
        self.entry = tk.Entry(self, width=20)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Create a Start Search Button and place it on the right (column 2)
        self.search_button = tk.Button(self, text="Start Search", command=self.start_search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

    def start_search(self):
        search_text = self.entry.get()
        print(f"Searching for: {search_text}")



if __name__ == "__main__":
    app = Ebook_app()
    app.mainloop()

# %%
# my solution for adding a scrolled Text widget for outputs and 
# writing the search term into the Text widget
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Ebook_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ebook Search")

        # Create a Label and place it on the left (column 0)
        self.label = tk.Label(self, text="Search for:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.entry = tk.Entry(self, width=30)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Create a Start Search Button and place it on the right (column 2)
        self.search_button = tk.Button(self, text="Start Search", command=self.start_search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Create a scrolled Text widget that spans all three columns and is 15 lines tall   
        self.scrolled_text = ScrolledText(self, width=40, height=15)
        self.scrolled_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10,)

    def start_search(self):
        search_text = self.entry.get()
        print(f"Searching for: {search_text}")

        # write search term into Text widget  
        self.scrolled_text.insert(tk.END, f"Searching for: {search_text}")



app = Ebook_app()
app.mainloop()

# %%
# My solution for adding a way to input a quality threshold number (1 - 100) 

# add a 2. row with a label and a scale (1 to 100, default 50)
# label goes in column 0, scale spans 1 and 2
# move Text to row 3

import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class Ebook_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ebook Search")

        # Create a Label and place it on the left (column 0)
        self.label = tk.Label(self, text="Search for Title:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.entry = tk.Entry(self, width=30)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Create a Start Search Button and place it on the right (column 2)
        self.search_button = tk.Button(self, text="Start Search", command=self.start_search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # for a row 2 add a label with Quality Threshold and a Scale widget from 0 to 100
        self.label = tk.Label(self, text="Quality Threshold:")
        self.label.grid(row=1, column=0, padx=10, pady=10, sticky="e")  
        self.scale = tk.Scale(self, from_=0, to=100, orient="horizontal") # start at 50
        self.scale.set(50)
        self.scale.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # Create a scrolled Text widget that spans all three columns and is 15 lines tall
        self.scrolled_text = ScrolledText(self, width=40, height=15)
        self.scrolled_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10,)

    def start_search(self):
        search_text = self.entry.get()
        print(f"Searching for: {search_text}")

        # write search term into Text widget  
        self.scrolled_text.insert(tk.END, f"Searching for: {search_text}")


app = Ebook_app()
app.mainloop()

# %% 
# Solution for convert the fuzzy_find function and to a method of the Ebook_app class 


# note that this will be flagged b/c it's indented as to be pasted into the class
    def fuzzy_find(self, search_term, n=1):
        matches = process.extract(search_term, self.df["Title"], scorer=fuzz.token_set_ratio, limit=n)
        first_match = matches[0] # grab only first match, ignore n for now
        text = first_match[0] # the text of the first match
        match_score = first_match[1] # the similarity score of the first match
        index = first_match[2] # the index in the data frame of the first match
        #print(f"searched for {search_term}\nbest match: {text}, {index}, {match_score}") # DEBUG a list of tuples (text, similarity score, index)
        return text, index, match_score

# %%
# Solution for the start_search method that uses the fuzzy_find method
    def start_search(self):
        search_term = self.entry.get()
        text, index, match = self.fuzzy_find(search_term)
        print(f"Best match for {search_term} is {text} with a score of {match}%")
        # if there is a > quality threhold match, print the book title, author, and summary,
        if match > self.scale.get():
            row = self.df.iloc[index]     # get the row of the best match using the index
            self.scrolled_text.insert(tk.END, f"The summary for {row['Title']} by {row['Author']} is:\n{row['Summary']}\n\n")
        else:
            self.scrolled_text.insert(tk.END, f"match of {match} is lower than {self.scale.get()}, no good match found!\n\n")


# %%
# My full solution
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import pandas as pd
from rapidfuzz import fuzz, process

class Ebook_app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ebook Search")

        # Create a Label and place it on the left (column 0)
        self.label = tk.Label(self, text="Search for Title:")
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        # Create an Entry Widget with a specific width (e.g., 30 characters)
        self.entry = tk.Entry(self, width=30)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        # Create a Start Search Button and place it on the right (column 2)
        self.search_button = tk.Button(self, text="Start Search", command=self.start_search)
        self.search_button.grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # for a row 2 add a label with Quality Threshold and a Scale widget from 0 to 100
        self.label = tk.Label(self, text="Quality Threshold:")
        self.label.grid(row=1, column=0, padx=10, pady=10, sticky="e")  
        self.scale = tk.Scale(self, from_=0, to=100, orient="horizontal") # start at 50
        self.scale.set(50)
        self.scale.grid(row=1, column=1, columnspan=2, padx=10, pady=10, sticky="ew")

        # Create a scrolled Text widget that spans all three columns and is 15 lines tall
        self.scrolled_text = ScrolledText(self, width=40, height=15)
        self.scrolled_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10,)

        # Read books.csv file into a DataFrame (see Python refresher 4)
        self.df = pd.read_csv('books.csv')  

    def fuzzy_find(self, search_term, n=1):
        matches = process.extract(search_term, self.df["Title"], scorer=fuzz.token_set_ratio, limit=n)
        first_match = matches[0] # grab only first match, ignore n for now
        text = first_match[0] # the text of the first match
        match_score = first_match[1] # the similarity score of the first match
        index = first_match[2] # the index in the data frame of the first match
        #print(f"searched for {search_term}\nbest match: {text}, {index}, {match_score}") # DEBUG a list of tuples (text, similarity score, index)
        return text, index, match_score

    def start_search(self):
        search_term = self.entry.get()
        text, index, match = self.fuzzy_find(search_term)
        print(f"Best match for {search_term} is {text} with a score of {match}%")
        # if there is a > quality threhold match, print the book title, author, and summary,
        if match > self.scale.get():
            row = self.df.iloc[index]     # get the row of the best match using the index
            self.scrolled_text.insert(tk.END, f"The summary for {row['Title']} by {row['Author']} is:\n{row['Summary']}\n\n")
        else:
            self.scrolled_text.insert(tk.END, f"match of {match} is lower than {self.scale.get()}, no good match found!\n\n")

        # scroll to bottom of text widget
        self.scrolled_text.see(tk.END)

app = Ebook_app()
app.mainloop()