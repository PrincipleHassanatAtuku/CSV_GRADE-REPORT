import csv

def open_csv():
    f = open("hassanat.csv", "r")
    return f
import csv

def create_reader(file_object):
    return csv.reader(file_object)
def get_header(data_reader):
    return next(data_reader)
