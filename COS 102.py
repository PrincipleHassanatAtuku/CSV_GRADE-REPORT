import csv

def open_csv():
    f = open("hassanat.csv", "r")
    return f
def get_header(data_reader):
    return next(data_reader)
