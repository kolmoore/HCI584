import tkinter as tk
import pandas as pd
from tkinter import scrolledtext
from rapidfuzz import fuzz, process

class Ebook_app(tk.Tk): # Inherit from tk.Tk, so can later use mainloop()
    def __init__(self):
        super().__init__() # Call the __init__() method of the parent class
        self.title("Playstore eBook Search") # Set the title of the window

        self.df = pd.read_csv('books.csv')   #  read the csv file into a data frame

        self.geometry("430x450")

        #Create an in app title
        self.heading = tk.Label(self, text="Playstore eBook Reader", font= ("Arial", 16),pady=5)
        self.heading.grid(row=1,column=2)
        
        # Create a Search Label
        self.label = tk.Label(self, text="Search for Title:", pady= 15,padx=5)
        self.label.grid(row=3,column=1)

        # Create an Search Entry Box
        self.entry = tk.Entry(self, width=35)
        self.entry.grid(row=3,column=2)
        self.entry.insert(0,"Business")

        # Create a Search Button
        self.search_button = tk.Button(self, text="Start Search", command=self.start_search,pady=5,padx=0)
        self.search_button.grid(row=3,column=3)

        # Create a Scrolled Text Messsage
        self.text_area = scrolledtext.ScrolledText(self, width=40,height= 15,font=("Times New Roman",12))
        self.text_area.grid(row=5,columnspan=4)
        #self.message = tk.Label(self, text = "Test Message", width=40,height= 15,justify ="left",relief="sunken",font=("Arial,14"),pady=15)
        #self.message.grid(row=4,columnspan=4)
        
        # Create a threshold slider
        self.thresh_label = tk.Label(self, text = "Search Threshold Value:")
        self.thresh_label.grid(row=6,column=1, columnspan=2)
        self.thresh = tk.DoubleVar()
        self.thresh.set(50)

        self.thresh_slider = tk.Scale(self, variable=self.thresh, from_=1, to=100, orient="horizontal", length=70)
        self.thresh_slider.grid(row=6, column=3)


    def start_search(self):
        # get your search term from the appropriate widget and use it with
        # the fuzzy_find method.
        # make sure to use the new fuzzy_find method, i.e. which doesn't take df as an argument anymore (see above)
        # if you used a scale, use self.scale.get() to get the current match quality value
        # write (insert) any good match results into the self.scrolled_text widget 
        # same for bad results, show what the percent is that didn't get over the quality threshold
        self.text_area.delete('1.0',tk.END)
        search_text = self.entry.get() # Get the text from the Entry Widget
        thresh = float(self.thresh_slider.get())
        self.text_area.insert(tk.INSERT, f"Searching for: {search_text}\n\n")

        text, index, match = self.fuzzy_find(search_text)


        if match > thresh:
            row = self.df.iloc[index] # find the row of the best match
            title, author, summary = row["Title"], row["Author"], row["Summary"]
            self.text_area.insert(tk.INSERT,f"Title: {title}\n\nAuthor: {author}\n\nSummary: {summary}\n\n\n")
            self.entry.delete(0,'end')
            self.entry.insert(0,"Enter a new title")
        else:
            self.text_area.insert(tk.INSERT,'Uh No! No good match found.  Try a different title or turn down the threshold for more flexibility in the results.')

    def fuzzy_find(self, search_term, n=1):

        matches = process.extract(search_term, self.df["Title"], scorer=fuzz.token_set_ratio, limit=n)
        first_match = matches[0] # grab only first match, ignore n for now
        text = first_match[0] # the text of the first match
        match_score = first_match[1] # the similarity score of the first match
        index = first_match[2] # the index in the data frame of the first match
    
        #print(f"searched for {search_term}\nbest match: {text}, {index}, {match_score}") # DEBUG a list of tuples (text, similarity score, index)
   
        return text, index, match_score

app = Ebook_app()
app.mainloop()