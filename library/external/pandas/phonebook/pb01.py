import pandas as pd           # import pandas library...
df = pd.read_csv("data.csv")  # load in data from external file called: data.csv
print(pd.DataFrame(df))       # printout data file as being a pandas data frame table(rows, cols) chart

# -----------------------------------------------------

# NOTE(1): If pandas library is not already installed;
#          then, open a MS DOS Prompt window/and, type command...
#          pip install pandas

# NOTE(2): Data file has to be stored inside of the same
#          directory folder/along with this program file.

# NOTE(3): The headers written at the start of the data file...;
#          is also the DataFrame headers printed out.

# The data file itself is written as follows...

# name,phone number
# Emergency,999
# NHS,118
# Samaritans,116 123

# The end DataFrame output result looks like this when printed out...

#         name     phone number
# 0  Emergency              999
# 1        NHS              118
# 2 Samaritans          116 123

# NOTE(4): The index numbers: 0,1,2...are being applied to the data, automatically; so, no need to write these.
# NOTE(5): With just 3 lines of Python/library code...; we've, successfully, gone and created a phonebook application.
 
