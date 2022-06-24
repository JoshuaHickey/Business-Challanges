
import csv

# Define lists 

list=[]
hex=[]
dec=[]
alldata=[]

# Index of first list element
n=0

# Open and read csv. Add releveant column to a list
with open(r'C:\Documents\*****.csv') as o:
    r = csv.DictReader(o)
    for col in r:
        list.append(col['vol_samples'])

for i in list:
    dec=[]
    # Calls the first row in 'vol_samples'. 
    firstrow = list[n]
    # Inserts a comma every 4th character.
    commas = str(','.join(firstrow[i:i+4] for i in range(0,len(firstrow),4)))
    # Seperates each hex code and stores in the list 'hex'.
    hex = commas.split(",")
    # Iterates through the 'hex' list and converts to decimal using the 'int()' method
    for i in hex:
        convertedvol = int(i,16)
        dec.append(convertedvol)
    # Appends 'dec' list to 'alldata' list
    alldata.append(dec)
    # Calls the next row element in 'list'
    n+=1
    
    # Write 'alldata' list to csv
    with open(r"C:\Documents\test.csv", "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(alldata)
