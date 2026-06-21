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
def calculate_averages(
        bio_tot,
        cos_tot,
        mth_tot,
        phy_tot,
        count):

    b_avg = bio_tot / count
    c_avg = cos_tot / count
    m_avg = mth_tot / count
    p_avg = phy_tot / count

    return b_avg, c_avg, m_avg, p_avgdef write_report(count,
                 b_avg,
                 c_avg,
                 m_avg,
                 p_avg):

    with open("report.txt", "w") as out:
        out.write("============ STUDENT PERFORMANCE REPORT ============\n")
        out.write(f"Total Students Processed: {count}\n\n")
        out.write(f"Average BIO102 Score: {b_avg:.2f}\n")
        out.write(f"Average COS102 Score: {c_avg:.2f}\n")
        out.write(f"Average MTH102 Score: {m_avg:.2f}\n")
        out.write(f"Average PHY102 Score: {p_avg:.2f}\n")
        out.write("====================================================\n")def display_report():
    print("Report successfully generated as 'report.txt'!")

    print("\n--- Displaying Generated Report ---")

    print(open("report.txt").read())
