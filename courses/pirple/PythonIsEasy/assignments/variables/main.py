"""
          COURSE: PythonIsEasy, (www.pirple.com)
         PROGRAM: Lesson 1/Assignment: Variables/Comments
        LANGUAGE: Python/Version: 3.8.6
---------------------------------------------------------
        COMPUTER: Home based Desktop PC
OPERATING SYSTEM: Windows 10 Professional
---------------------------------------------------------
          AUTHOR: Mr. Paul Ramnora
        LOCATION: London, UK
           EMAIL: pramnora@yahoo.com
---------------------------------------------------------
          GITHUB: https://www.github.com/pramnora
    RELATED CODE: https://github.com/pramnora/python/blob/master/courses/pirple/PythonIsEasy/assignments/variables/main.py
---------------------------------------------------------
    FILE CREATED: 14:56 05/10/2020
    LAST UPDATED: 19:28 05/10/2020
"""

"""
     EXPLANATION:-
                  The assignment asks to write code which illustrates...
                  - the use of Python multi-line comments 
                  - the use of Python single line comments
                  - the use of variables in relation to describing one of your favourite songs
                  - variable types should include: strings/integers/decimals(floats)
                  - after assigning the variable values/you should also print the variables out
                  - finally, zip up the file/and, upload it to be marked online 
"""

# ----------------------------
# *** Variable declarations...
# ----------------------------

# --- string...

strProgramTitle = "Song details"
strSongTitle = "The First Time Ever I Saw Your Face" 
strWriter = "Ewan Macoll"
strReleased ="March 7, 1972"
strGenre = "Folk song, Soul, Vocal jazz"
strFilm = "Play Misty For Me"
strDirector = "Clint Eastwood"
strProducer = "Joel Dorn"
strSinger = "Roberta Flack"
strRecordLabel = "Atlantic 2864"
strGrammyAwards = "Record of the Year/Song of the Year"
strBillboardRank = "No 1/Hot 100 single of the year for 1972"
strReference = "https://en.wikipedia.org/wiki/The_First_Time_Ever_I_Saw_Your_Face"

# --- integer...

intWrittenDate = 1957
intRecorded = 1968
intFilmDate = 1972

# --- float...

fltLength = 5.22

# --- boolean

bolHit = True

# -------------------
# *** Sub-routines...
# -------------------

def printUnderline():
   strUnderscore = "-" #...local variable declaration
   print(strUnderscore*100)
  
# -------------------
# *** Main program...
# -------------------

# *** Printout...

print("       PROGRAM: ",strProgramTitle)
printUnderline()
print("    Song Title: ",strSongTitle)
print("        Writer: ",strWriter)
print("  Written date: ",intWrittenDate)
print("      Released: ",strReleased)
print("      Recorded: ",intRecorded)
print("         Genre: ",strGenre)
printUnderline()
print("          Film: ",strFilm)
print("     Film Date: ",intFilmDate)
print("      Director: ",strDirector)
print("      Producer: ",strProducer)
print("        Singer: ",strSinger)
print("  Record Label: ",strRecordLabel)
print("        Length: ",fltLength)
printUnderline()
print("           Hit: ",bolHit)
print(" Grammy Awards: ",strGrammyAwards)
print("Billboard Rank: ",strBillboardRank)
printUnderline()
print("     Reference: ",strReference)
