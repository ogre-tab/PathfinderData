import sys
import csv
import os

# TODO: add error checking

# check if a string can be an int
def isInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

# replace any characters that might cause issues
def clean(s):
    # remove extra whitespace
    s = s.strip()
    if '\\' in s: # this needs to be first if other characters are to be escaped
        s = s.replace('\\','\\\\')
    if '"' in s:
        s = s.replace('"','\\"')
    return s

# store the output and write opening json tags
json = []

# argument
filename = sys.argv[1]

filename, ext = os.path.splitext(filename)
output = filename + '.json'
filename = filename + ext

# open the file
with open(filename, mode="r", encoding="utf-16") as csvfile:
    # create the csv reader
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # get the header line, and move to next row
    header = next(reader)
    # loop through all the rows in the csv
    for row in reader:
        # add the json text
        json.append('{')
        # empty line to create
        line = ""
        # go through each item in the row
        for i in range(len(row)):
            # write the line depending on if the value is a int or not
            if isInt(row[i]):
                line += '"' + header[i].strip() + '": ' + row[i] + ','
            else:
                line += '"' + header[i].strip() + '": "' + clean(row[i]) + '",'
        # remove the last comma
        line = line.rstrip(',')
        # add the built string to the json list
        json.append(line + '},\n')
    # remove the last comma from the last item added
    json[-1] = json[-1].strip().rstrip(',')
# write the closing json tags
json.append('\n')

# open the output file
with open(output, "w") as file:
    # write all the items in the json list to file
    file.writelines(json)
