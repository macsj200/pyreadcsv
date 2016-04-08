import csv, os, sqlalchemy
file_dir = "/Users/maxjohansen/Downloads/Forecasting Project"
file_raw_dir = os.path.join(file_dir, "Raw")

contents1 = os.listdir(file_dir)
contents2 = os.listdir(file_raw_dir)

files = [os.path.join(file_dir,filename) for filename in contents1 if not os.path.isdir(os.path.join(file_dir,filename))] + [os.path.join(file_dir,file_raw_dir) for filename in contents2 if not os.path.isdir(os.path.join(file_dir,file_raw_dir))]

for file in files:
    with open(files[0], encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            pass
            # print(', '.join(row))
