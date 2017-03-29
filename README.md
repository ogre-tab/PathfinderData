# PathfinderData
Data should be created in spreadsheets that then can be used to ouput rows.
The headers will become the json fields, and the row data will be the field properties.

The pfData.py file will convert a csv into a json file using the above format.
The input file of the python program will change the file etension from csv to json and place the
file in the same location as the source file.

usage: python pfData.py input.csv

The files names will need to be added to the GtkCharacterSheet classes to be read in.
All files should begin with pf, then sorted by the content of the data using more dots.
Example: pf.class.sorcer.json
This file would reside in the classes folder, in a subfolder for sorcerer.