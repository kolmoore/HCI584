# Python HW2 part 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements: (res, err)
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# - must have 3 parts: <A>@<B>.<C>
# - A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# - B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# - C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react as above (OK or error message) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16 chars"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
 # Create some error messages so we don't have to think about it later
    err_mess1 = "Must have 3 parts: address@domain.suffix"
    err_mess2 = "Address must have alpha numeric chars." # (test: isalnum()) 
    err_mess3 = "Address must have between 3 and 16 chars." # (test: len())
    err_mess4 = "Domain must have alpha numeric chars." # (test: isalnum())
    err_mess5 = "Domain must have between 2 and 8 chars." # (test: isalnum()) 
    err_mess6 = "Suffix must be one of these:  com edu org gov"

    # Load the acceptable suffixes onto a list so we don't have to remember those
    suffs = ["com","edu","org","gov"]
    

    first_split = s.split(sep='@')  # Attempting to split the email string into two parts seperated by the location of the @ symbol

    if len(first_split) < 2:
        return(1,err_mess1)         # If we don't have atleast two parts the @ symbol wasn't present
    
    else:
        name = first_split[0]       # If we do have two parts we MAY have a name, we can grab the first part of list and do some checks

        if len(name) == 0:          # First, check if a value exists, if not all 3 parts of the email weren't there (missing address)
            return(1,err_mess1)     
        if not(name.isalnum()):     # Next, check if the name is alphanumeric, if not throw an error.  
            return(2,err_mess2)    # Note: if this check went first it would trigger a misleading error in the event of a missing name
        if len(name)>16 or len(name)<3:     # Finally check if the name is within the length requirements
                return(3,err_mess3)
        else:


            second_split = first_split[1].split(sep='.')    # Only if the name checks out do we attempt to create a second split

            if len(second_split) < 2:                       # Again we check if the split was made as this indicates if a '.' was present and therefor if 
                return(1,err_mess1)                         # the email had the correct form and parts
            else:
                domain = second_split[0]                    # We grab both parts of the list this time since they are both interesting
                suffix = second_split[1]

                if len(domain) == 0 or len(suffix) == 0:    # Check if both values exist
                    return(1,err_mess1)
                if not(domain.isalnum()):                   # Check if the domain is alphanumeric
                    return(4,err_mess4)
                if len(domain) > 8 or len(domain) < 2:      # Check if the domain is within the length requirements
                    return(5,err_mess5)
                if suffs.count(suffix) != 1:                # Check if the suffix matches one on our list of acceptable suffixes
                    return(6,err_mess6)
                else:
                    return(None,"Email Seems Legit")        # If we've made it this far we're out of checks, the email must be good.

    



# tests, including edge cases (incomplete? add more!)
email_list = ["charding@iastate.edu", 
    "chris.edu",
    "chris@edu",
    "@bla.edu",
    "throatwobblermangrove@mpfc.org", 
    "chris@X.com",
    "chris.harding@iastate.edu",
    "chris@pymart.biz",
    "chris@letsgo!.org",
    "chris@megasavings.org",
    "tc@tank.com",
    ]

# validate each email from the list
for e in email_list:
    r, s = is_valid_email_address(e) 
    if r == None:
        print(e, s) # OK
    else:
        print(f"{e} - error: {s}, error code: {r}") # Error

