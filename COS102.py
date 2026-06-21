import csv

def open_csv():
    f = open("hassanat.csv", "r")
    return f
import csv

def create_reader(file_object):
    return csv.reader(file_object)
def get_header(data_reader):
    return next(data_reader)
def initialize_totals():
    bio_tot = 0
    cos_tot = 0
    mth_tot = 0
    phy_tot = 0
    count = 0

    return bio_tot, cos_tot, mth_tot, phy_tot, countdef process_records(data_reader,
                    bio_tot,
                    cos_tot,
                    mth_tot,
                    phy_tot,
                    count):

    for record in data_reader:
        if not record:
            continue

        bio_tot += int(record[1])
        cos_tot += int(record[2])
        mth_tot += int(record[3])
        phy_tot += int(record[4])
        count += 1

    return bio_tot, cos_tot, mth_tot, phy_tot, count
