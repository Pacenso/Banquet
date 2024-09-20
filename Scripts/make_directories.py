import os

# MUST CHANGE FOR EACH USE CASE
path = "Path/to/destination"

for i in range(1, 100): # number of files with respective names to create
    if i < 10:
        # MUST CHANGE FOR EACH USE CASE
        os.mkdir(path + str(i))
    else:
        # MUST CHANGE FOR EACH USE CASE
        os.mkdir(path + str(i))

print("Successfully created directories")
