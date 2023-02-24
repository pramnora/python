import pandas as pd                # import pandas library...
df_file1 = pd.read_csv("data.csv") # load in data from external file called: data.csv
print(pd.DataFrame(df_file1))      # printout data file as being a pandas data frame table(rows, cols) chart

# -----------------------------------------------------

# NOTE(1): If pandas library is not already installed;
#          then, open a MS DOS Prompt window/and, type command...
#          pip install pandas

# NOTE(2): Data file has to be stored inside of the same
#          directory folder/along with this program file.

# NOTE(3): The headers written at the start of the data file...;
#          is also the DataFrame headers printed out.

# The data file itself is written as follows...

# name,age
# Fred,5
# Harry,7
# John,9

# The end DataFrame output result looks like this when printed out...

#    name age
# 0  Fred 5
# 1  Harry 7
# 2  John 9

