import csv, os
from dateutil.parser import parse
file_dir = "/Users/maxjohansen/Downloads/Forecasting Project"
file_raw_dir = os.path.join(file_dir, "Raw")

contents = os.listdir(file_raw_dir)

files = [os.path.join(file_raw_dir,filename) for filename in contents]

with open('vis/data.csv', 'w') as csvoutfile:
    fieldnames = ['date', 'sum']
    writer = csv.DictWriter(csvoutfile, fieldnames=fieldnames)
    # writer.writeheader()
    for file in files:
        # Skip 2012 data (for now)
        if '2012' in file:
            continue
        with open(file, encoding="latin-1") as csvfile:
            the_sum = 0.0
            reader = csv.reader(csvfile)
            row_num = 0
            price_index = -1
            for row in reader:
                if row_num == 0:
                    price_index = [rowname.strip().replace(' ','').lower() for rowname in row].index("invoicetotal")
                else:
                    the_sum = the_sum + float(row[price_index])
                row_num = row_num + 1
            prettyfilename = file.lower().strip().replace(' ','').replace('_','').replace('ucsf','').replace('.csv.xls','')
            prettyfilename = prettyfilename[prettyfilename.index('data') + len('data'):]
            date = parse(prettyfilename)
            datestring = date.strftime('%Y-%m')
            print({'date': datestring, 'sum': the_sum})
            writer.writerow({'date': datestring, 'sum': the_sum})
