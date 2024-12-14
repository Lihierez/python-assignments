# Write a command line tool that can download data from NCBI. You can download from the nucleotide database as we did in the lecture, 
# but it would be much more interesting if you used some of the other databases available on NCBI. e.g.:
# python ncbi.py  --database nucleotide --term TERM --number NUMBER
# The database can default to "nucleotide", ther number can default to 10.

# Search for the TERM and download up to NUMBER items. Save each item in its own file. Print the names of the files. 
# Also save the date, the database, the search term, the number asked for and the total number of items found in a csv file. So if you run the command twice:

# python ncbi.py  --database genome --term Orchid --number 3
# python ncbi.py  -cauliflower
# you'd get something like this:
# date,term,max,total
# 2024-05-30 17:20:21,genome,Orchid,3,527341
# 2024-05-30 18:12:34,nucleotide,cauliflower,10,32781

from Bio import Entrez
import argparse
import csv
from datetime import datetime


#command line arguments: dataset, term, number of records, email
parser = argparse.ArgumentParser()
parser.add_argument('--database', default='nucleotide', help='NCBI database')
parser.add_argument('--term', required=True, help='Search term')
parser.add_argument('--number', type=int, default=10, help='Number of records')
parser.add_argument('--email', required=True, help='User email for NCBI API')
args = parser.parse_args()

Entrez.email = args.email

#prefom the search
handle = Entrez.esearch(db=args.database, term=args.term, retmax=args.number)
record = Entrez.read(handle)
handle.close()

# search result (for output)
total_found = int(record["Count"])
ids = record["IdList"]

# download and save records
for id in ids:
    handle = Entrez.efetch(db=args.database, id=id, rettype="fasta", retmode="text")
    filename = f"{args.database}_{id}.fasta"
    with open(filename, 'w') as f:
        f.write(handle.read())
    print(f"Saved: {filename}")
    handle.close()

#current date and time (for output)
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# print output
print(f"{current_time},{args.database},{args.term},{args.number},{total_found}")

# log the search in CSV
with open('searches.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    if f.tell() == 0:  # If file is empty, write header
        writer.writerow(['database', 'term', 'max', 'total'])
    writer.writerow([args.database, args.term, args.number, total_found])

