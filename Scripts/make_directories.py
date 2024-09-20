import os

# MUST CHANGE FOR EACH USECASE
path = "/Users/roccojemilo/Library/Mobile Documents/com~apple~CloudDocs/Madison/Classes/2024 Fall Semester/stat_240/homework"

for i in range(1, 16):
    if i < 10:
        # MUST CHANGE FOR EACH USE CASE
        os.mkdir(path + "/hw0" + str(i))
    else:
        # MUST CHANGE FOR EACH USE CASE
        os.mkdir(path + "/hw" + str(i))

print("Successfully created directories")
